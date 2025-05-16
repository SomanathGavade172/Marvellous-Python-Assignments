'''
    4. Write a program which accept one number form user and return addition of its factors.

    Input  : 12 
    Output : 16 (1+ 2+ 3+ 4+ 6)

'''
# Function Defination
def SumFactors(Value):
    Sum = 0
    # Logic to calculate addition of its factors 
    for i in range(1, (Value // 2) + 1):
        if(Value % i == 0):
            Sum = Sum + i
    return Sum

# Main Function
def main():
    print("Enter a Number : ")
    No = int(input())

    Result = SumFactors(No)        # Function Call

    print("Addition of Factors are : ", Result)

# Starter
if __name__ == "__main__":
    main()