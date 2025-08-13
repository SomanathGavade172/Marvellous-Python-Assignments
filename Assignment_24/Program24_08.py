'''
    Q8. Plot a histogram of math marks.

'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    data = {'Name' : ['Amit', 'Sagar', 'Pooja'], 'Math' : [85,90,75], 'Science' : [92,88,80], 'English' : [75,80,82]}

    df = pd.DataFrame(data)     # dataframe 'df' created
    
    df['Total'] = df['Math'] + df['Science'] + df['English']

    df.insert(0, 'Gender', ['Male', 'Male', 'Female'])
       
    # One Hot Encoding on Gender Column
    df = pd.get_dummies(df, columns=['Gender'], dtype=int, drop_first=True)

    # print("\nData Frame after One-Hot-Encoding : ")
    print(df)

    # Grouping
    grouped_data = df.groupby(['Gender_Male'])['Total'].mean()
    
    CntPass = 0

    df['Status'] = 'Fail'
    for i in range(len(df)):
        if(df.at[i, 'Total'] >= 250):
            df.at[i, 'Status'] = 'Pass'
            CntPass += 1

    print("Total Students who passed : ", CntPass)

    # historgram of math marks
    plt.figure(figsize=(8,6))
    plt.hist(df['Math'], bins= 10, color='skyblue')
    plt.xlabel('Math Marks')
    plt.ylabel('Frequency of Marks')
    plt.title("Marvellous Maths Histogram")
    plt.show()

if __name__ == "__main__":
    main()
