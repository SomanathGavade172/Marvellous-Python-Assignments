'''
    10. Write a program which accept number from user and return addition of digits in that number.

    Input  : 5187934 

    Output : 37

'''

# Function Defination
def  SumDigit(Value):
    Sum = 0

    # Logic to Calculate sum of Digits
    while(Value > 0):
        Rem = Value % 10

        Sum = Sum + Rem     # Sum of Digits

        Value = Value // 10

    return Sum

# Main Function
def main():
    print("Enter a number : ")
    No = int(input())

    Result = SumDigit(No)       # Function Call

    print("Addition of digits is : ", Result)

# Starter
if __name__ == "__main__":
    main()