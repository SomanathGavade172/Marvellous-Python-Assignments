import pandas as pd

from sklearn.preprocessing import LabelEncoder

from sklearn.cluster import KMeans

import matplotlib.pyplot as plt


def main():
    df = pd.read_csv('student-mat.csv')

    print(df.head())
    print(df.shape)

    encoder = LabelEncoder()
    df['internet_encoded'] = encoder.fit_transform(df['internet'])

    X = df[['studytime', 'failures', 'absences', 'health', 'internet_encoded', 'G1', 'G2', 'G3']]
    
    print(X.head())
    print(X.shape)

    WCSS = []           # WCSS - Within Cluster Sum of Squares : for elbow method to get the appropriate number of clusters

    # Finalised Cluseter after Visualisation - 4
    model = KMeans(n_clusters=4, init='k-means++', n_init=10, random_state=42)
    Y_pred = model.fit_predict(X)

    print("Value of Y_pred : ", Y_pred)

    
    plt.scatter(X[Y_pred == 0,0], X[Y_pred == 0,1], s = 100, c = 'red', label = 'Setosa')
    plt.scatter(X[Y_pred == 1,0], X[Y_pred == 1,1], s = 100, c = 'blue', label = 'Versicolor')
    plt.scatter(X[Y_pred == 2,0], X[Y_pred == 2,1], s = 100, c = 'green', label = 'Virginica')

    plt.scatter(model.cluster_centers_[:,0], model.cluster_centers_[:,1], s=50, c = 'yellow', label = 'centroid')

    plt.legend()
    plt.show()
    
if __name__ == "__main__":
    main()