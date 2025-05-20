'''
    Q3. Accept a number from the user and print its multiplication table up to 10.

    Expected Input:
                        Enter a number: 7
    Expected Output :
                        7 x 1 = 7
                        7 x 2 = 14
                        ...
                        7 x 10 = 70

'''

# Function Defination
def MultiplicationTable(Value):
    # Logic to Print Multiplication Table
    for i in range(1, 11):
        print(Value, "x", i , "=", Value * i )

# Main Function
def main():
    print("Enter a Number : ")
    # Handle ValueError
    try:        
        No = int(input())

    except(ValueError):
        print("Invalide Input..! Enter Numeric Values..!")
        return

    MultiplicationTable(No)     # Function Call

# Starter
if __name__ == "__main__":
    main()                  # Function Call