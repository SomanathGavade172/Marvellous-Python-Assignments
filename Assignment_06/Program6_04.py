'''
    Q4. Accept a number and print its factorial using a for loop.

    Expected Input  :
            Enter  a  number  : 5

    Expected Output :
            Factorial of 5 is : 120

'''

def Factorial(Value):
    # Filter if number is -ve.
    if(Value < 0):
        Value = -(Value)

    # Logic to calculate Factorial.
    Fact = 1
    for i in range(1,Value + 1):
        Fact = Fact * i

    return Fact

# Main Function
def main():
    print("Enter a Number : ")
    # Input must be an integer
    try:
        
        No = int(input())
    
    except(ValueError):
        print("Invalide Input ..! Enter Numeric Values..!")
        return 

    Ret = Factorial(No)     # Function Call

    print("Factorial of", No, "is : ", Ret)

# Starter
if __name__ == "__main__":
    main()                  # Function Call