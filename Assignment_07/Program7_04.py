'''
    Q4. Accept a list of numbers and use reduce() (from functools) to find the product of all numbers.

    Expected Input  :
        Enter list  : 2 3 4

    Expected Output :
            Product : 24

'''

from functools import reduce

# Function Defination
Product = lambda No, Pro : No * Pro     # Logic Product of all Numbers.

def main():

    List = []       # Empty List

    print("Enter Number of Elements : ")

    # Accept Integer Numbers
    try:
        # Accept Number of Elements from User.
        Size = int(input())

        print("Enter",Size, "Numbers : ")

        # Accept Numbers from User.
        for i in range(Size):
            No = int(input())
            List.append(No)

    except(ValueError):
        print("Invalide Input..! Enter Numeric Values..!")
        return
    
    RList = reduce(Product, List)       # Function Call
    print("Product : ", RList)

if __name__ == "__main__":
    main()                  # Function Call