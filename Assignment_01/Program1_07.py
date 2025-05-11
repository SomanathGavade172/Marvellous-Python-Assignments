''' 
    7. Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.

    Input  : 8 
    Output : False

    Input  : 25 
    Output : True
'''
# Function Defination
def ChkDivisible(No):
    # Logic to Check Number is Divisible by 5
    if(No % 5 == 0):
        return True
    else:
        return False

# Main Function
def main():
    Value = int(input("Enter a Number : "))

    Result = ChkDivisible(Value)        # Function Call

    print(Result)

# Starter
if __name__ == "__main__":
    main()                             # Function Call