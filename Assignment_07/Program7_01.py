'''
    Q1. Write two lambda functions  :
            • One to calculate square of a number
            • Another to calculate cube of a number

    Expected Input  :

            Enter a number  : 3

    Expected Output  :
            Square   : 9
            Cube     : 27

'''
# Function Defination
Square = lambda Value : Value ** 2      # Logic Square of Number.

# Function Defination
Cube = lambda Value : Value ** 3        # Logic Cube of Number.

# Main Function
def main():
    print("Enter a Number : ")
    
    # Accept Integer Numbers.
    try:

        No = int(input())

    except(ValueError):
        print("Invalide Input..! Enter Numeric Values..!")
        return

    # Display Result
    Ret = Square(No)            # Function Call
    print("Square : ", Ret)

    # Display Result
    Ret = Cube(No)              # Function Call
    print("Cube : ", Ret)

# Starter
if __name__ == "__main__":
    main()                      # Function Call