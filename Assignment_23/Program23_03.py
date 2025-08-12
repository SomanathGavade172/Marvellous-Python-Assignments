'''
    Q3: Add a new column 'Total' to the DataFrame as the sum of all subject marks.

    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

'''

import pandas as pd

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    Line = "*" * 50

    df = pd.DataFrame(data)

    print(Line)
    print("Data with Total Marks :\n")
    df['Total'] = df['Math'] + df['Science'] + df['English']
    print(df)
    print(Line)

if __name__ == "__main__":
    main()