'''
    Q6: Sort the DataFrame by 'Total' marks in descending order.

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

    df['Total'] = df['Math'] + df['Science'] + df['English']
    
    sorted_df = df.sort_values(by='Total', ascending=False)

    print(Line)
    print("Data sorted by Total marks (descending):\n")
    print(sorted_df)
    print(Line)

if __name__ == "__main__":
    main()
