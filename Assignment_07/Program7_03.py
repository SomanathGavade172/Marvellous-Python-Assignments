'''
    Q3. Accept a list of numbers and use filter() to keep only even numbers.

    Expected Input  :
            Enter list   : 1 2 3 4 5 6

    Expected Output :
            Even numbers : [2, 4, 6]
'''
# Function Defination
Even = lambda No : No % 2 == 0      # Logic Even Numbers.

# Main Function
def main():
    List = []       # Empty List

    print("Enter Number of Elements : ")
    # Accept Integer Numbers.
    try:
        # Accept Number of Elements from User.
        Size = int(input())

        # accept Number from User
        print("Enter", Size, "Numbers : ")
        for i in range(Size):
            No = int(input())
            List.append(No)

    except(ValueError):
        print("Invalide Input..! Enter Numeric Values..!")
        return 
    
    FList = list(filter(Even, List))        # Function Call
    print("Even List is : ", FList)

# Starter 
if __name__ == "__main__":
    main()                  # Function Call
