'''
    2. Factorial Using Recursion Write a recursive function to calculate factorial of a number.

    factorial(5) → 120

'''
# Global Variable
iFact = 1
i = 1

# Function Defination
def CalculateFactorial(iValue):
    
    global iFact, i
    
    # Logic to Calculate Factorial
    if(i <= iValue):
        iFact = iFact * i
        i += 1

        CalculateFactorial(iValue)      # Recursive Call

# Main Function
def main():

    print("Enter a Number : ")

    try:
        # Accept Number from User.
        iNo = int(input())

    except(ValueError):
        print("Invalide Input..! Enter Numeric Values")
        return

    CalculateFactorial(iNo)            # Function Call

    print("Factorial is : ", iFact)

# Starter
if __name__ == "__main__":
    main()                  # Function Call
