'''
    1.Write a program which contains one lambda function which accepts one parameter and return power of two.

    Input  : 4 
    Output : 16

    Input  : 6 
    Output : 64

'''

# Lambda Function to Calculate Power of Two
Power = lambda Value : 2 ** Value

# Main Function
def main():
    print("Enter a Number : ")

    # Accept only Integer Numbers
    try:
        # Accept number from User
        No = int(input())

    except(ValueError):
        print("Invalid Input ..! Enter Numeric Values..!")
        return
    
    Ret = Power(No)         # Function Call

    print("Power of Two is : ", Ret)

# Starter
if __name__ == "__main__":
    main()                  # Function Call