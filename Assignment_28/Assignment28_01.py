import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import accuracy_score, confusion_matrix


def MarvellousWinePredictor(Datapath):
    df = pd.read_csv(Datapath)

    print(df.head())
    print("Dimensions of the Dataset : ", df.shape)
    
    df.dropna(inplace=True)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    scaler = StandardScaler()
    x_scale = scaler.fit_transform(X)

    X_train, X_test, Y_train, Y_test = train_test_split(x_scale, Y, test_size=0.2, random_state=42)


    Accuracy_scores = []
    K_range = range(1, 21)

    for k in K_range:
        model = KNeighborsClassifier(n_neighbors = k)
        model.fit(X_train, Y_train)
        Y_pred = model.predict(X_test)
        accuracy = accuracy_score(Y_test, Y_pred)
        Accuracy_scores.append(accuracy)
    
    best_k = K_range[Accuracy_scores.index(max(Accuracy_scores))]
    print("Best value of k is : ", best_k)

    model = KNeighborsClassifier(n_neighbors = k)
    model.fit(X_train, Y_train)
    Y_pred = model.predict(X_test)
    accuracy = accuracy_score(Y_test, Y_pred)

    print("Final best accuracy : ", accuracy*100)

    cm = confusion_matrix(Y_test, Y_pred)
    print(cm)

def main():
    MarvellousWinePredictor('WinePredictor.csv')

if __name__ == "__main__":
    main()