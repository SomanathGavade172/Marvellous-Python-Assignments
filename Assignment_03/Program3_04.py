'''
    4. Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.

    Input : 

        Number of elements  :  11
        Input Elements      :  13 5 45 7 4 56 5 34 2 5 65
        Element to search   :  5

    Output : 3

'''

# Function Defination
def CountFrequency(Value1):
    List = []                # Empty List

    # Logic to Accept number from user and store to List.
    print("Enter the Elements : ")

    for i in range(Value1):
        No = int(input())
        List.append(No)

    # Logic to Count Frequency of Number.
    print("Enter Element to Search : ")
    Value2 = int(input())
    Count = 0

    for i in List:
        if(i == Value2):
            Count += 1
    return Count

# Main Function
def main():
    print("Enter a Number of Elements : ")
    No = int(input())

    Result = CountFrequency(No)         # Function Call

    print("Frequency of Element are : ", Result)

# Starter
if __name__ == "__main__":
    main()