'''
    3. Write a program which accept one number from user and return its factorial.

        Input  :  5 
        Output : 120

'''
# Function Defination
def Factorial(Value):
    Ans = 1
    # Logic to calculate Factorial
    for i in range(1,Value + 1):
        Ans = Ans * i
    return Ans

# Main Function
def main():
    print("Enter a Number : ")
    No = int(input())

    Result = Factorial(No)      # Function Call

    print("Factorial is : ", Result)

# Starter
if __name__ == '__main__':
    main()