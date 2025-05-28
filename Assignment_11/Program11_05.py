'''
    5. Count Zeros in a Number (Recursively) Write a recursive function to count how many zeros are in the given number.

    count_zeros(1020300) → 4

'''
# Global Variable
iCount = 0

# Function Defination
def CountZero(iValue):
    global iCount

    # Logic to Count Zero
    if(iValue != 0):
        iRemender = iValue % 10

        if(iRemender == 0):
            iCount = iCount + 1

        iValue = iValue // 10

        CountZero(iValue)           # Recursive Call


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

    CountZero(iNo)            # Function Call

    print("Count of Zero is : ", iCount)

# Starter
if __name__ == "__main__":
    main()                  # Function Call