'''
    1. Write a program which contains one lambda function which accepts one parameter and return power of two.

        Input  : 4 
        Output : 16
        
        Input  : 6 
        Output : 64

'''
# Lambda Function to Calculate Power of Two (2^n)
PowerX = lambda A : 2 ** A

# Main Function
def main():
    print("Enter Number : ")
    No = int(input())

    Result = PowerX(No)         # Function Call

    print("Power is : ", Result)

# Starter
if __name__ == "__main__":
    main()
