'''
    2. Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.

    Input  :

        Number of elements  : 7
        Input Elements      : 13 5 45 7 4 56 34

    Output : 56

'''
# Function Defination
def FindMaximum(Value):
    List = []       # Empty List    

    # Logic to Accept Number from user and Store into List.
    print("Enter a Elements : ")
    
    for i in range(Value):
        No = int(input())
        List.append(No)

    # Logic to Find MAximum Element.
    iMax = List[0]

    for i in List:
        if(iMax < i):
            iMax = i
    return iMax

# Main Function
def main():
    No = int(input("Enter a Number of Elements : "))

    Result = FindMaximum(No)        # Function Call

    print("Maximum Number is : ", Result)

# Starter
if __name__ == "__main__":
    main()