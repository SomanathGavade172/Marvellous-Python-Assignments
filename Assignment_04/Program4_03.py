'''
    3. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter
    should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all that
    numbers.

    Input List        = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
    List after filter = [76, 89, 86, 90, 70]
    List after map    = [86, 99, 96, 100, 80]
    Output of reduce  = 6538752000

'''
# Import reduce from Module functools
from functools import reduce

# MAin Function
def main():

    List = []       # Empty List

    print("Enter Number of Element : ")
    Size = int(input())

    # Logic Accept Number from User
    print("Enter a Number : ")
    for i in range(Size):
        No = int(input())
        List.append(No)

    # Logic of FILTER
    FList = list(filter(lambda No : (70 <= No or No >= 90), List))
    print("Filter output : ", FList)

    # Logic of MAP
    MList = list(map(lambda No : No + 10, FList))
    print("Map Output : ", MList)

    # Logic of REDUCE
    RList = reduce(lambda A, B : A * B, MList)
    print("Reduce output : ", RList)

# Starter
if __name__ == "__main__":
    main()                  # Function Call