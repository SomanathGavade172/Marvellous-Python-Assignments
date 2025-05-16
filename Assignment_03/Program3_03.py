'''
    3. Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.

    Input  : 

        Number of elements  :  4
        Input Elements      :  13 5 45 7

    Output : 5

'''

# Function Defination
def FindMinimum(Value):
    List = []       # Empty List

    print("Enter a Elements : ")

    # Logic to Accept Number from user and Store into List.
    for i in range(Value):
        No = int(input())
        List.append(No)

    # Logic to find Minimum Number
    iMin = List[0]

    for i in List:
        if(iMin > i):
            iMin = i

    return iMin

# Main Function
def main():
    print("Enter Number Of Elements : ")
    No = int(input())

    Result = FindMinimum(No)        # Function Call

    print("Minimum Element is : ", Result)

# Starter    
if __name__ == "__main__":
    main()