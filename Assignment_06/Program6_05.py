'''
    Q5. Accept a number from the user and check whether it is prime or not.

    Expected Input  :
                        Enter a number  : 11
    Expected Output :
                        11 is a prime number.

'''

# Function Defination
def ChkPrime(Value):
    # Logic to check Prime Number.
    for i in range(2, Value):
        if(Value % i == 0):
            return False
    
    return True

# Main Function
def main():
    print("Enter a Number : ")
    No = int(input())

    Ret = ChkPrime(No)      # Function Call

    # Result Display
    if(Ret == True):
        print(No, "is a Prime Number.")
    else:
        print(No, "Is Not Prime Number.")

# Starter
if __name__ == "__main__":
    main()                  # Function Call