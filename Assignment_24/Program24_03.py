'''
    Q3. Group students by gender and calculate average marks.

'''


import pandas as pd
import numpy as np


def main():
    data = {'Name' : ['Amit', 'Sagar', 'Pooja'], 'Math' : [85,90,75], 'Science' : [92,88,80], 'English' : [75,80,82]}

    df = pd.DataFrame(data)     # dataframe 'df' created
    
    df['Total'] = df['Math'] + df['Science'] + df['English']

    df.insert(0, 'Gender', ['Male', 'Male', 'Female'])
        
    # One Hot Encoding on Gender Column
    df = pd.get_dummies(df, columns=['Gender'], dtype=int, drop_first=True)

    # Grouping
    grouped_data = df.groupby(['Gender_Male'])['Total'].mean()
    print("Data after Grouping Gender and Marks : ")
    print(grouped_data)

if __name__ == "__main__":
    main()
