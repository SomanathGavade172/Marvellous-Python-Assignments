'''
    1. Print Numbers Using Recursion Write a recursive function to print numbers from 1 to N.

    Expected Output (for n=5) :
                                1 2 3 4 5

'''
# global Variable
i = 1

# Function Defination
def Display(iVaues):
    global i 

    # Logic to Print Number from 1 to N
    if(i <= iVaues):
        print(i, end = " ")
        i = i + 1

        Display(iVaues)     # Recursive Call

# Main Function
def main():

    print("Enter a Number : ")

    try:
        # Accept Number from User.
        iNo = int(input())

    except(ValueError):
        print("Invalide Input..! Enter Numeric Values")
        return

    Display(iNo)            # Function Call

# Starter
if __name__ == "__main__":
    main()                  # Function Call
