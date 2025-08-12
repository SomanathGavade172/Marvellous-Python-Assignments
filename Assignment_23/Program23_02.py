'''
    Q2: Use the DataFrame from Q1 and print descriptive statistics using .describe().
    
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
    print("Basic Statastics is :\n", df.describe())
    print(Line)

if __name__ == "__main__":
    main()