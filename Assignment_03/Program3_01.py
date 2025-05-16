'''
1.Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.

    Input          : 

        Number of elements :  6
        Input Elements     :  13 5 45 7 4 56

    Output         : 130

'''

# Function Defination
def SumList(Value):
    List = []       # Empty LIst
    Sum = 0

    print("Enter a Numbers : ")

    # Logic to Calculate addition of all elements from that List.
    for i in range(Value):
        No = int(input())
        List.append(No)

        Sum = Sum + List[i]

    return Sum

# Main Function
def main():
    Size = int(input("Enter Number of Elements : "))

    Result = SumList(Size)      # Function Call

    print("Addition is : ", Result)

# Starter
if __name__ == "__main__":
    main()

    

    
        