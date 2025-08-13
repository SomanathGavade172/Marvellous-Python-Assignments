'''
    Q2. Create a gender column and perform one-hot encoding.

'''

import pandas as pd
import numpy as np


def main():
    data = {'Name' : ['Amit', 'Sagar', 'Pooja'], 'Math' : [85,90,75], 'Science' : [92,88,80], 'English' : [75,80,82]}

    df = pd.DataFrame(data)     # dataframe 'df' created
    print(df)
    # print(df.describe())

    df.insert(0, 'Gender', ['Male', 'Male', 'Female'])
    print("\nDataframe after inserting Gender column : ")
    print(df)
    
    # One Hot Encoding on Gender Column
    df = pd.get_dummies(df, columns=['Gender'], dtype=int, drop_first=True)

    print("\nData Frame after One-Hot-Encoding : ")
    print(df)

if __name__ == "__main__":
    main()
