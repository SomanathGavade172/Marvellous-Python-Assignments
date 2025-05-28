'''
    6. Sum of First N Natural Numbers Write a recursive function to calculate sum from 1 to n.

    sum_n(5) → 15

'''
# Global Variable
iSum = 0
i = 1

# Function Defination
def CalculateSum(iValue):
    global iSum , i

    # Logic to Calculate Sum of First Natural.
    while(i <= iValue):
        iSum = iSum + i
        i = i + 1

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

    print("Sum of First Natural Numbers is : ", iSum)

# Starter
if __name__ == "__main__":
    main()                  # Function Call