'''
    Q7. Normalize 'Age' column using Min-Max Scaling.

    data = {'Age': [18, 22, 25, 30, 35]}

'''

import pandas as pd

def main():
    data = {'Age' : [18, 22, 25, 30, 35]}
    df = pd.DataFrame(data)
    
    df['Age_normalized'] = (df['Age'] - df['Age'].min()) / (df['Age'].max() - df['Age'].min())

    print(df)

if __name__ == "__main__":
    main()