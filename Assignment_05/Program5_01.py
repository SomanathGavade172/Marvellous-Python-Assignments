'''
    Q1. Arithmetic Operations on Two Numbers Write a program to accept two integers from the user and display their:

    • Sum
    • Difference
    • Product
    • Division

    Expected Input:
        Enter first number   : 10
        Enter second number  : 2

    Expected Output:
        Sum           :  12
        Difference    :   8
        Product       :  20
        Division      :  5.0

'''
# Function Defination Of Sum
def Sum(No1, No2):
    Ans = No1 + No2
    return Ans

# Function Defination Of Product
def Difference(No1, No2):
    Ans = No1 - No2
    return Ans

# Function Defination Of Multiplication
def Multiplication(No1, No2):
    Ans = No1 * No2
    return Ans

# Function Defination Of Division
def Division(No1, No2):
    Ans = No1 / No2
    return Ans

# Main Function
def main():
    # Accept Two numbers from User.
    Value1 = int(input("Enter First Number : "))
    Value2 = int(input("Enter Second Number : "))

    Ret = Sum(Value1, Value2)               # Function Call
    print("Sum : ", Ret)

    Ret = Difference(Value1, Value2)           # Function Call
    print("Difference : ", Ret)

    Ret = Multiplication(Value1, Value2)    # Function Call
    print("Multiplication : ", Ret)

    Ret = Division(Value1, Value2)          # Function Call
    print("Division : ", Ret)

# Starter
if __name__ == "__main__":
    main()                  # Function Call