'''
    2. Write a program which contains one lambda function which accepts two parameters and return its multiplication.

    Input  :  4  3 
    Output :  12

    Input  :  6  3 
    Output :  18

'''
# Lambda Function to Calculate Multiplication of Two Numbers,
Multiplication = lambda A, B : A * B

# Main Function
def main():
    print("Enter First Number : ")

    # Accept only Integer Numbers
    try:
        # Accept number from User
        No1 = int(input())
    except(ValueError):
        print("Invalid Input..! Enter Numeric Values..!")
        return
    
    print("Enter Second Number : ")

    # Accept only Integer Numbers
    try:
        # Accept number from User
        No2 = int(input())
    except(ValueError):
        print("Invalid Input..! Enter Numeric Values..!")
        return
    
    Ret = Multiplication(No1, No2)      # Function Call

    print("Multiplication is : ", Ret)

# Starter
if __name__ == "__main__":
    main()                  # Function Call