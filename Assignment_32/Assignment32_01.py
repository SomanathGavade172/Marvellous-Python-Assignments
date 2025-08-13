import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score, confusion_matrix

def main():
    Border = "-"*100
    df_true = pd.read_csv('True.csv')
    df_fake = pd.read_csv('Fake.csv')

    print(Border)
    print("True df null report : ")
    print(df_true.isnull().sum())

    print("\nFake df null report : ")
    print(df_fake.isnull().sum())

    df_true = df_true.assign(Label = 1)
    
    print("\n\n")
    
    df_fake = df_fake.assign(Label = 0)
    
    df = pd.concat([df_fake, df_true])
        
    X = df['title'] + " " + df['text'] + " " + df['subject'] + " " + df['date']
    Y = df['Label']


    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)    

    # TF-IDF (Term Frequency-Inverse Document Frequency)  - used to convert the text into numerical format
    vectorizer = TfidfVectorizer()
    X_train_new = vectorizer.fit_transform(X_train)
    X_test_new = vectorizer.transform(X_test)

    '''
    Dictionary will store the accuracy of their respective model
    '''
    accuracy_dict = {}

    dt_model = DecisionTreeClassifier()
    lr_model = LogisticRegression()

    dt_model.fit(X_train_new, Y_train)
    Y_pred = dt_model.predict(X_test_new)

    accuracy = accuracy_score(Y_test, Y_pred)
    
    print(Border)
    print("Accuracy using Decision Tree Classifier: ", accuracy*100)
    accuracy_dict['Decision_Tree'] = accuracy
    conf = confusion_matrix(Y_test, Y_pred)
    print("Confusion matrix of Decision Tree Classifier :")
    print(conf)

    
    lr_model.fit(X_train_new, Y_train)
    Y_pred = lr_model.predict(X_test_new)

    accuracy = accuracy_score(Y_test, Y_pred)
    print("Accuracy using Logistic Regression: ", accuracy*100)
    accuracy_dict['Logistic_Regression'] = accuracy
    conf = confusion_matrix(Y_test, Y_pred)
    print("Confusion matrix of Logistic Regression :")
    print(conf)


    voting = VotingClassifier(
        estimators=[
            ('lr', lr_model),
            ('dt', dt_model)
        ],
        voting='hard'
    )

    voting.fit(X_train_new, Y_train)
    Y_pred = voting.predict(X_test_new)

    accuracy = accuracy_score(Y_test, Y_pred)

    print(f"Accuracy using Voting Classification(Hard) is : {accuracy*100}")
    accuracy_dict['Voting_Clf_hard'] = accuracy*100
    conf = confusion_matrix(Y_test, Y_pred)
    print("Confusion matrix of Hard Voting Classifier :")
    print(conf)

    
    voting = VotingClassifier(
        estimators=[
            ('lr', lr_model),
            ('dt', dt_model)
        ],
        voting='soft'
    )

    voting.fit(X_train_new, Y_train)
    Y_pred = voting.predict(X_test_new)

    accuracy = accuracy_score(Y_test, Y_pred)

    print(f"Accuracy using Voting Classification(Soft) is : {accuracy*100}")
    accuracy_dict['Voting_Clf_soft'] = accuracy*100
    conf = confusion_matrix(Y_test, Y_pred)
    print("Confusion matrix of Soft Voting Classifier :")
    print(conf)

    # Comparison of the Accuracies
    Max_accuracy_model = None
    Max_accuracy_value = 0

    for key, values in accuracy_dict.items():
        Max_accuracy_value = max(Max_accuracy_value, accuracy_dict[key])
        if(Max_accuracy_value == accuracy_dict[key]):
            Max_accuracy_model = key

    print(Border)
    print(f"Maximum Accuracy : ")
    print(f"{Max_accuracy_model} : {Max_accuracy_value}")
    print(Border)    

if __name__ == "__main__":
    main()