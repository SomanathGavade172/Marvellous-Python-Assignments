'''
    Q1. Detect outliers in the 'Salary' column using the IQR method.

    data = {'Salary': [25000, 27000, 29000, 31000, 50000, 100000]}

'''

import pandas as pd
import numpy as np

# Detect Outliers using IQR method
def main():
    data = {'Salary' : [25000, 27000, 29000, 31000, 50000, 100000]}
    df = pd.DataFrame(data)

    print(df.head())
    print("Dimension : ", df.shape)
    
    Q1 = df['Salary'].quantile(0.25)
    Q3 = df['Salary'].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5*IQR
    upper = Q3 + 1.5*IQR

    print("IQR : ", IQR)
    print("lower bound of the outlier : ", lower)
    print("upper bound of the outlier: ", upper)



if __name__ == "__main__":
    main()