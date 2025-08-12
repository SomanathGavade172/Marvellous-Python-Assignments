'''
    Q5: Replace 'Pooja' with 'Puja' in the 'Name' column.

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
    print("Replace 'Pooja' with 'Puja' is :\n")
    df['Name'] = df['Name'].replace('Pooja', 'Puja')
    print(df)
    print(Line)

if __name__ == "__main__":
    main()