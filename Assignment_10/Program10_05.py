'''
    5. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter
    should filter out all prime numbers. Map function will multiply each number by 2. Reduce will return Maximum number from that numbers. (You can also use normal functions instead of
    lambda functions).

    Input List         =  [2, 70 , 11, 10, 17, 23, 31, 77]
    List after filter  =  [2, 11, 17, 23, 31]
    List after map     =  [4, 22, 34, 46, 62]
    Output of reduce   =   62

'''
# Import Module reduce from functools
from functools import reduce

# Function Defination
def ChkPrime(Values):
    if(Values <= 1):
        return False

    # Logic to Check Prime Number
    for i in range(2, Values):
        if(Values % i == 0):
            return False
    return True
 
# Logic to Map
MapData = lambda Values : Values * 2

# Function Defination
def ChkMax(Values1, Values2):
    if(Values1 > Values2):
        return Values1
    else:
        return Values2
    
# Main Function
def main():
    Data = []       # Empty List

    print("Enter Number of Elements : ")

    # Accept Integer Numbers only.
    try:
        # Accept Number of Elements from User.
        Size = int(input())
    except(ValueError):
        print("Invalid Input..! Enter Numeric Values..!")
        return
    
    print("Enter", Size, "Number : ")

    # Accept Integer Numbers only.
    try:
        # Accept Number of Elements from User.
        for i in range(Size):
            No = int(input())
            Data.append(No)         # Accept Number into List
    except(ValueError):
        print("Invalid Input..! Enter Numeric Values..!")
        return
    
    # Apply Filter to Data
    FData = list(filter(ChkPrime, Data))        # Function Call
    print("List After Filter : ", FData)
    
    # Apply Map to Filter Data(FData)
    MData = list(map(MapData, FData))           # Function Call
    print("List After Map is : ", MData)

    # Apply Reduce to Map Data(MData)
    RData = reduce(ChkMax, MData)               # Function Call
    print("Reduced output is : ", RData)

# Starter
if __name__ == "__main__":
    main()                  # Function Call