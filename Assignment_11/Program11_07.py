'''
    7. Print Pattern Using Recursion (Right Triangle) Write a recursive function to print the following pattern:

        *
        * *
        * * *
        * * * *

'''
# Global Variable
i = 1
j = 1

# Function Defination
def DisplayPattern(iValue):
    
    global i

    # Logic to print *
    if(i <= iValue):
        global j

        if(j <= i):
            print("*", end = " ")
            j = j + 1

            DisplayPattern(iValue)      # Recursive Call

        else:

            print()
            i += 1
            j = 1

            DisplayPattern(iValue)      # Recursive Call

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

    DisplayPattern(iNo)            # Function Call

# Starter
if __name__ == "__main__":
    main()                  # Function Call