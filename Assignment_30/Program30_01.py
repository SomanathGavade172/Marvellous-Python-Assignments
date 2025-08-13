import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split


def BankFullModel(DataPath):
    line = '-'*90
    df = pd.read_csv(DataPath, delimiter=';')
    df.columns = df.columns.str.replace('"', '').str.strip()

    print(line)
    print('Description of DataSet:')
    print(line)
    print(df.describe())
    print(line)

    df.drop(columns=['default', 'contact', 'previous','previous', 'poutcome'])
    
    # Encoding 
    for col in df.select_dtypes(include='object'):
        df[col] = LabelEncoder().fit_transform(df[col])

    print(df.head())

    # Splitting Dataset
    X = df.drop(columns=['y'])
    y = df['y']

    # Scaling the data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

    # Training model
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    # Predicting
    y_pred = model.predict(X_test)

    print(line)
    acc = accuracy_score(y_test, y_pred)
    print("Accuracy: ", acc*100)
    print(line)
    cm = confusion_matrix(y_test, y_pred)
    print(line)
    print("Confusion Matrix: ")
    print(cm)
    print(line)


def main():
    BankFullModel('bank-full.csv')

if __name__ == '__main__':
    main()