'''
    Q1: Create a DataFrame for student marks and print basic information like shape, columns, and data types.

    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
'''

import pandas as pd

def main():
    Data = {
        'Name' : ['Amit', 'Sagar', 'Pooja'],
        'Math' : [85, 90, 78],
        'Science' : [92, 88, 80],
        'English' : [75, 85, 82]
    }

    Line = "*" * 50

    df = pd.DataFrame(Data)

    print(Line)
    print("Shape of Data Frame : ", df.shape)

    print(Line)
    print("Colomns are : \n", df.columns.tolist())

    print(Line)
    print("Data Type are : \n", df.dtypes)
    print(Line)

if __name__ == "__main__":
    main()