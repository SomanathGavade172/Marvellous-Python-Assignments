import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler

def DiabetesPredictor(Datapath):
    line = '-'*80
    df = pd.read_csv(Datapath)
    print(line)
    print('Sample Dataset :')
    print(line)
    print(df.head())
    print(line)
    print('Dimensions of Dataset :')
    print(df.shape)
    print(line)

    print('Description of Dataset :')
    print(line)
    print(df.describe())
    print(line)

    # Visualisation
    plt.figure(figsize=(10,5))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title('Diabetes Predictor')
    plt.show()

    # Features and target
    x = df.drop(columns=['Outcome'], axis=1)
    y = df['Outcome']

    # Scaling
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)

    # Splitting
    x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.2, random_state=42)

    # Model with more iterations
    model = LogisticRegression()
    model.fit(x_train, y_train)
    
    y_pred = model.predict(x_test)

    # Results
    Accuracy = accuracy_score(y_pred, y_test)
    ConfMatrix = confusion_matrix(y_pred, y_test)
    print('Accuracy Score is : ', Accuracy*100)
    print(line)
    print('Confusion Matrix :')
    print(ConfMatrix)
    print(line)

def main():
    DiabetesPredictor('diabetes.csv')

if __name__ == '__main__':
    main()