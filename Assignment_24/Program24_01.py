'''
    Q1. Normalize the 'Math' scores using Min-Max scaling.

'''

import pandas as pd
import numpy as np


def main():
    data = {'Name' : ['Amit', 'Sagar', 'Pooja'], 'Math' : [85,90,75], 'Science' : [92,88,80], 'English' : [75,80,82]}

    df = pd.DataFrame(data)     # dataframe 'df' created
    print(df)
    print(df.describe())
    
    # X_normalized = (X - X_min) / (X_max - X_min)
    df['Math_Normalized'] = (df['Math'] - df['Math'].min()) / (df['Math'].max() - df['Math'].min())

    print("Dataframe after Normalizing Math Scores : ")
    print(df)


if __name__ == "__main__":
    main()

