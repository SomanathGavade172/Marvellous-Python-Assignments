import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

def MarvellousAdvertise(Datapath):
    df = pd.read_csv(Datapath)

    print("Dataset Sample is : ")
    print(df.head())

    print("Clean the dataset")
    df.drop(columns= ['Unnamed: 0'], inplace= True)        # inplace : manipulate in the existing dataset only
    
    print("Updated Dataset is :")
    print(df.head())

    print("Missing values in each column : ")
    print(df.isnull().sum())

    print("Statistical Summary : ")
    print(df.describe())

    print("Correlation Matrix")
    print(df.corr())
    # when there are multiple independent variables, then we have to consider the correlation between the independent variables with the Dependent Variable

    plt.figure(figsize=(10,5))
    # heatmap is used to show correlation
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title("Marvellous Correlation Heatmap")
    plt.show()

    sns.pairplot(df)
    plt.suptitle("Pairplot of Features", y = 1.02)
    plt.show()

    X = df[['TV', 'radio', 'newspaper']]
    Y = df[['sales']]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    MSE = mean_squared_error(Y_test, Y_pred)
    RMSE = np.sqrt(MSE)
    r2 = r2_score(Y_test, Y_pred)

    print("Mean-squared-error : ", MSE)
    print("Root-mean-squared-error : ", RMSE)
    print("R-Square : ", r2)

    print("Model Coefficient are : ")
    for col, coef in zip(X.columns, model.coef_):
        print("{col} : {coef}")
    
    print("Intercept c is : ", model.intercept_)

    plt.figure(figsize=(8,5))
    plt.scatter(Y_test, Y_pred, color='blue')
    plt.xlabel("Actual Sales")
    plt.ylabel("Predicted Sales")
    plt.title("Marvellous Advertisement")
    plt.grid(True)
    plt.show()

def main():
    MarvellousAdvertise('Advertising.csv')

if __name__ == "__main__":
    main()