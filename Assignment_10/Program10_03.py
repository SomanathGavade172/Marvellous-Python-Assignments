'''
    3. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter
    should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all that
    numbers.

    Input List        = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
    List after filter = [76, 89, 86, 90, 70]
    List after map    = [86, 99, 96, 100, 80]
    Output of reduce  = 6538752000

'''
# Import Module reduce from functools
from functools import reduce

# Logic of Filter
FilterData = lambda Values : (Values >= 70 and Values <= 90)

# Logic of Map
MapData = lambda Values : Values + 10

# Logic of Reduce
ReduceData = lambda Value1, Value2 : Value1 * Value2

# Main Function
def main():
    Data = []       # empty List

    print("Enter Number Elements : ")

    # Accept only Integer Numbers
    try:
        # Accept Number Elements from User.
        Size = int(input())
    except(ValueError):
        print("Invalid Input..! Enter Numeric Values..!")
        return
    
    print("Enter", Size, "Numbers : ")
    for i in range(Size):

        # Accept only Integer Numbers
        try:
            No = int(input())
            Data.append(No)         # Accept Numbers into the List
        except(ValueError):
            print("Invalid Input..! Enter Numeric Values..!")
            return

    # Apply Filter to Data
    FData = list(filter(FilterData, Data))          # Function Call
    print("List after filter is : ", FData)

    # Apply Map to Filter data (FData)
    MData = list(map(MapData, FData))               # Function Call
    print("List After Map is : ", MData)

    # Apply Reduce to Map data (MData)
    RData = reduce(ReduceData, MData)               # Function Call
    print("Output of Reduce is : ", RData)

# Main Function
if __name__ == "__main__":
    main()                  # Function Call