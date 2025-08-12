'''
    Q4: Display students who scored more than 85 in Science.

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
    print("students who scored more than 85 in Sciences are :\n", df[df['Science'] > 85])
    print(Line)

if __name__ == "__main__":
    main()