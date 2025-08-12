'''
    Q7: Create a bar plot of student names vs total marks.

    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

'''

import pandas as pd
import matplotlib.pyplot as plt

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

    print(Line)
    print(df)
    print(Line)

    plt.figure(figsize = (10, 5))
    plt.bar(df['Name'], df['Total'], color='blue')
    plt.xlabel("Student Name")
    plt.ylabel("Total Marks")
    plt.title("Total Marks of Students")
    plt.grid(False)
    plt.show()

if __name__ == "__main__":
    main()

