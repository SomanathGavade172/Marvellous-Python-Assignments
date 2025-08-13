'''
    Q2. Detect column data types and convert 'Age' from float to int.
    
    data = {'Name': ['A', 'B', 'C'], 'Age': [21.0, 22.0, 23.0]}

'''

import pandas as pd
import numpy as np

def main():
    data = {'Name' : ['A', 'B', 'C'], 'Age' : [21.0, 22.0, 23.0]}
    df = pd.DataFrame(data)

    print(df.head())
    print("Dimension : ", df.shape)

    print("\nColumn Data Types : ")    
    print(df.dtypes)

    print(df['Age'].values)

    df['Age'] = df['Age'].astype(int)
    print("Datatype of 'Age' Column after changing : ")
    print(df)



if __name__ == "__main__":
    main()