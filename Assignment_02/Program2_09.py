'''
    9. Write a program which accept number from user and return number of digits in that number.

    Input  : 5187934 
    
    Output : 7

'''
# Function Defination
def CountDigit(Value):
    Count = 0
    
    # Filter If Value == 0 then Digit Count is 1
    if(Value == 0):
        return 1
    
    # Logic to Count Digits
    while(Value != 0):
        Count += 1
        Value = Value // 10

    return Count

# Main Function
def main():
    print("Enter a Number : ")
    No = int(input())

    Result = CountDigit(No)     # Function Call

    print("Number of Digit are : ", Result)

# Starter
if __name__ == "__main__":
    main()