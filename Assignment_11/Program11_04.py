'''
    4. Power Function Using Recursion Write a recursive function to calculate x^n.

    power(2, 3) → 8

'''
# Global Variable
Power = 1
i = 0

# Function Defination
def CalculatePower(iValue):
    
    global Power , i    

    # Logic to Calculate Power 
    while(i < iValue):
        Power = Power * 2
        i = i + 1

        CalculatePower(iValue)      # recursive Call

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

    CalculatePower(iNo)            # Function Call

    print("Power is : ", Power)

# Starter
if __name__ == "__main__":
    main()                  # Function Call