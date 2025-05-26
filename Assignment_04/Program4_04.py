'''
    4. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter
    should filter out all such numbers which are even. Map function will calculate its square. Reduce will return addition of all that numbers.

    Input List        =  [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]    
    List after filter =  [2, 4, 4, 2, 8, 10]
    List after map    =  [4, 16, 16, 4, 64, 100]
    Reduce Output is  =   204

'''
# Import reduce from Module functools
from functools import reduce

# MAin Function
def main():

    List = []       # Empty List

    print("Enter a Number of Elements : ")
    Size = int(input())

    # Logic Accept number from User
    print("Enter a Elements : ")
    for i in range(Size):
        No = int(input())
        List.append(No)

    # Logic of FILTER
    FList = list(filter(lambda No : (No % 2 == 0), List))       # Lambda function call by Filter
    print("Filter Output is : ", FList)

    # Logic of MAP
    MList = list(map(lambda No : No ** 2, FList))               # Lambda function call by MAP
    print("Map Output is : ", MList)

    # Logic of REDUCE
    RList = reduce((lambda A, B : A + B), MList)                # Lambda function call by REDUCE
    print("Reduce Output is : ", RList)

# Starter
if __name__ == "__main__":
    main()                  # Function call
