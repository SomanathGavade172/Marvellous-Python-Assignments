'''
    4. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter
    should filter out all such numbers which are even. Map function will calculate its square. Reduce will return addition of all that numbers.

    Input List        =  [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]    
    List after filter =  [2, 4, 4, 2, 8, 10]
    List after map    =  [4, 16, 16, 4, 64, 100]
    Reduce Output is  =   204

'''
# Import Module reduce from functools
from functools import reduce

# Logic of Filter
FilterData = lambda Values : Values % 2 == 0

# Logic of Map
MapData = lambda Values : Values ** 2

# Lofic of Reduce
ReduceData = lambda Values1, Values2 : Values1 + Values2

# Main Function
def main():
    Data = []       # Empty List

    print("Enter Number of Elements : ")
    # Accept Integer Numbers.
    try:
        # Accept Number of Elements from User.
        Size = int(input())
    except(ValueError):
        print("Invalid Input ..! Enter Numeric Values..!")
        return
    
    print("Enter", Size, "Numbers : ")
    for i in range(Size):
        # Accept Integer Numbers.
        try:
            # Accept Numbers from User
            No = int(input())
            Data.append(No)         # Numbers accept into List
        except(ValueError):
            print("Invalid Input..! Enter Numeric Values..!")
            return
    
    # Apply Filter to Data
    FData = list(filter( FilterData, Data))     # Function Call 
    print("List After Filter is : ", FData)

    # Apply Map to Filter Data(FData)
    MData = list(map(MapData, FData))           # Function Call
    print("List after Map is : ", MData)

    # Apply Reduce to Map Data(MData)
    RData = reduce(ReduceData, MData)           # Function Call
    print("Reduced Output is : ", RData)

# Starter
if __name__ == "__main__":
    main()                  # Function Call