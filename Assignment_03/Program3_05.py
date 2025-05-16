'''
    5. Write a program which accept N numbers from user and store it into List. Return addition of all prime numbers from that List. Main python file accepts N numbers from user and pass each
    number to ChkPrime() function which is part of our user defined module named as MarvellousNum. Name of the function from main python file should be ListPrime().

    Input  : 

        Number of elements :  11
        Input Elements     :  13 5 45 7 4 56 10 34 2 5 8

    Output : 32 (13 + 5 + 7 +2 + 5)

'''
# Import Module MarvellousNum
from MarvellousNum import ChkPrime

# Function Defination
def ListPrime(Value):
    List = []           # Empty List

    # Logic to accept input from user
    print("Enter a Elements : ")
    for i in range(Value):
        No = int(input())
        List.append(No)

    # Logic to Check Prime Number and Return Addition of Prime Number.
    Add = 0
    for i in List:
        if(ChkPrime(i) ):       # Function Call From Module 
            Add = Add + i
    return Add

# Main Function
def main():
    print("Enter Number of Elements : ")
    Size = int(input())

    Result = ListPrime(Size)        # Function Call

    print("Addtion of Prime Number is : ", Result)

# Starter
if __name__ == "__main__":
    main()