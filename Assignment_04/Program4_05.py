'''
    5. Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter
    should filter out all prime numbers. Map function will multiply each number by 2. Reduce will return Maximum number from that numbers. (You can also use normal functions instead of
    lambda functions).

    Input List         =  [2, 70 , 11, 10, 17, 23, 31, 77]
    List after filter  =  [2, 11, 17, 23, 31]
    List after map     =  [4, 22, 34, 46, 62]
    Output of reduce   =   62

'''
# Import reduce from module functools
from functools import reduce

# Function Defination
def ChkPrime(Value):
    if(Value <= 1):
        return False

    # Logic to Check Prime Number
    for i in range(2, Value):
        if(Value % i == 0):
            return False
    return True

# Function Defination
def ChkMax(Value1, Value2):
    # Logic to Check Maximum Number
    if(Value1 > Value2):
        return Value1
    else:
        return Value2

# Main Function
def main():

    List = []       # Empty List

    print("Enter Number of Elements : ")
    Size = int(input())

    # Accept Numbers from User
    print("Enter a Element : ")
    for i in range(Size):
        No = int(input())
        List.append(No)

    # Logic of Filter
    FList = list(filter(ChkPrime, List))            # Function Call (ChkPrime)
    print("Filter Output is : ", FList)

    # Logic of Map
    MList = list(map(lambda No : No * 2, FList))    # Lambda Function Call by MAP     
    print("Map Output is : ", MList)

    # Logic of Reduce
    RList = reduce(ChkMax, MList)                   # Function Call (ChkMax)
    print("Reduce Output is : ", RList)

# Starter
if __name__ == "__main__":
    main()                  # Function call