'''
    Q2. Accept a list of integers from the user and use the map() function to double each value.

    Expected Input   :
        Enter list   : 1 2 3 4 5

    Expected Output  :
        Doubled list : [2, 4, 6, 8, 10]

'''
# Function Defination
Double = lambda X : X * 2       # Logic Double each Value.

# Main Function
def main():
    List = []       # Empty List

    print("Enter Number of Elements : ")

    # Accept Integer Numbers
    try:
        # Number of elements in the List[]
        Size = int(input())

        print("Enter the Elements : ")
        # Accept Numbers from User.
        for i in range(Size):
            No = int(input())
            List.append(No)
        
    except(ValueError):
        print("Enter Valide Input..! Enter Numeric Value..!")

    MList = list(map(Double, List))         # Map() Function call 
    print("Doubled List is : ", MList)

# Starter
if __name__ == "__main__":
    main()                  # Function Call

