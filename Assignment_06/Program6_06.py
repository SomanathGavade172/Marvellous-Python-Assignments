'''
    Q6. Print Triangle Pattern using Nested Loops

    Expected Output:

                    *
                    * *
                    * * *
                    * * * *
'''

# Function Defination
def DisplayPattern(Value):
    # Filter
    if(Value < 0):
        Value = -(Value)

    # Logic to display Pattern
    for i in range(1,Value + 1):
        for j in range(i):
            print("*", end = " ")

        print()

# Main Function
def main():
    print("Enter a Number : ")
    # Input Must be Integer.
    try:

        No = int(input())

    except (ValueError):
        print("Invalide Input..! Enter Numeric Value..!")
        return

    DisplayPattern(No)     # Function Call

# Starter
if __name__ == "__main__":
    main()                  # Function Call