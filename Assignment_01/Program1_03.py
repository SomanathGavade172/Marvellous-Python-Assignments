'''
    3. Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.

    Input  : 11  5 
    Output : 16

'''
# Function Defination
def Add(No1, No2):
    # Logic to Calculate Addition of Two Numbers
    Ans = No1 + No2
    return Ans

# Main Function
def main():
    print("Enter First Number : ")
    Value1 = int(input())

    print("Enter Second Number : ")
    Value2 = int(input())

    Result = Add(Value1, Value2)    # Function Call

    print("Addition is : ", Result)

# Starter
if __name__ == "__main__":
    main()                          # Function Call