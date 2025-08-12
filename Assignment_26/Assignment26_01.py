#  Play Predictor Dataset
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def CalculateAccuracy(X_train, X_test,Y_train, Y_test): 
    accuracyData = []
    K_range = range(2,16)
    for i in K_range:
        model = KNeighborsClassifier(n_neighbors=i)
        model.fit(X_train, Y_train)

        Y_pred = model.predict(X_test)

        accuracy = accuracy_score(Y_test, Y_pred)
        accuracyData.append(accuracy)
    
    # K_range vs Accuracy visual overview
    plt.figure(figsize=(8,6))
    plt.plot(K_range, accuracyData, marker = 'o', linestyle = '--')
    plt.xlabel("Range of K")
    plt.ylabel("Accuracy")
    plt.title("PlayPredict CaseStudy K_range vs Accuracy")
    plt.grid(True)
    plt.xticks(K_range)
    plt.show() 
    
    best_k = K_range[accuracyData.index(max(accuracyData))]
    print(f"Best Accuracy is on value K = {best_k}")

    model = KNeighborsClassifier(n_neighbors=best_k)
    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test, Y_pred)
    print(f"Accuracy on K = {best_k} is ", accuracy*100)

    conf_matrix = confusion_matrix(Y_test, Y_pred)
    print("\nConfusion Matrix : ")
    print(conf_matrix)    

def  MarvellousPlayPredictor(datapath):
    df = pd.read_csv(datapath)
    print("Dataset : ")
    print(df.head())
    print("Shape : ", df.shape)

    # dropping the unnecessary column : Cleaning dataset
    df.drop(labels=['Unnamed: 0'], axis='columns', inplace=True)
    
    print("\nSum of Missing Values in the Dataset :")
    print(df.isnull().sum())

    # Encoding
    label_encoder = LabelEncoder()
    df['Play'] = label_encoder.fit_transform(df['Play'])
    df['Whether'] = label_encoder.fit_transform(df['Whether'])
    df['Temperature'] = label_encoder.fit_transform(df['Temperature'])
    print("\nFinal Updated Dataset : ")
    print(df.head())
    print("\nStatistical Data : ")
    print(df.describe())

    X = df.drop(labels=['Play'], axis='columns')
    Y = df['Play']

    # Data Splitting
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    CalculateAccuracy(X_train, X_test, Y_train, Y_test)

def main():
    MarvellousPlayPredictor('PlayPredictor.csv')

if __name__ == "__main__":
    main()