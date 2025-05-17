'''
    2. Write a program which contains one lambda function which accepts two parameters and return its multiplication.

    Input  :  4 3 
    Output :  12

    Input  :  6 3 
    Output :  18

'''

# Lambda Function to Calculate Multiplication
MultiplicationX = lambda A, B : A * B

# MAin Function
def main():
    print("Enter First Number : ")
    No1 = int(input())

    print("Enter Second Number : ")
    No2 = int(input())

    Result = MultiplicationX(No1, No2)      # Function Call

    print("Multiplication is : ", Result)

# Starter
if __name__ == "__main__":
    main()                  # Function Call