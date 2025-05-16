'''
    5. Write a program which accepts one number from user and checks whether it is prime or not.

    Input  : 5 
    Output : It is Prime Number

'''
# Function Defination
def ChkPrime(Value):
    # Filter 
    if(Value <= 1):
        return False
    
    # Logic to Check number is Prime or Not
    for i in range(2, Value):
        if(Value % i == 0):
            return False
    return True

# Main Function
def main():
    print("Enter a Number : ")
    No = int(input())

    Result = ChkPrime(No)       # Function Call

    if (Result == True):
        print("It is Prime Number")
    else:
        print("It is Not a Prime Number")

# Starter
if __name__ == "__main__":
    main()
