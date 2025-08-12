'''
    Q6: Replace multiple values in a column using a dictionary.

    data = {'Grade': ['A+', 'B', 'A', 'C', 'B+']}

    Replace as
    'A+': ‘Excellent'
    'A': 'Very Good’
    'B+': ‘Good'
    'B': ‘Average'
    'C': 'Poor'

'''

import pandas as pd

def main():
    data = {'Grade' : ['A+', 'B', 'A', 'C', 'B+']}
    df = pd.DataFrame(data)
    print(df)
    
    df['Grade'] = df['Grade'].map({'A+' : 'Excellent', 'A' : 'Very Good', 'B+' : 'Good', 'B' : 'Average', 'C' : 'Poor'})
    print(df)

if __name__ == "__main__":
    main()