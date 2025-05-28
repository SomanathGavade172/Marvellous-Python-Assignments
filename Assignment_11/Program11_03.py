'''
    3. Sum of Digits  Write a recursive function to calculate the sum of digits of a number.

    sum_of_digits(1234) → 10

'''
# Golobal Variable
iSum = 0

# Function Defination
def CalculateSum(iValue):
    
    global iSum

    # Logic to Calculate Sum of Digits
    if(iValue != 0):
        iRemnder = iValue % 10

        iSum = iSum + iRemnder

        iValue = iValue // 10

        CalculateSum(iValue)        # Recursive Call
    
# Main Function
def main():

    print("Enter a Number : ")

    try:
        # Accept Number from User.
        iNo = int(input())

        if(iNo < 0):
            print("Invalid input..! Please Enter +Ve Number..!")
            return

    except(ValueError):
        print("Invalide Input..! Enter Numeric Values")
        return

    CalculateSum(iNo)            # Function Call

    print("Sum is : ", iSum)

# Starter
if __name__ == "__main__":
    main()                  # Function Call