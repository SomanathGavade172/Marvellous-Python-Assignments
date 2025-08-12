'''
    Q8: Plot a line chart of marks for 'Amit' across all subjects.a

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

    print(Line)
    print(df)
    print(Line)

    amit_row = df[df['Name'] == 'Amit']
    subjects = ['Math', 'Science', 'English']
    marks = amit_row[subjects].values.flatten()

    plt.figure(figsize=(10, 5))
    plt.plot(subjects, marks, color='green')
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.title("Amit's Marks Across Subjects")
    plt.grid(False)
    plt.ylim(0, 100)
    plt.show()

if __name__ == "__main__":
    main()
