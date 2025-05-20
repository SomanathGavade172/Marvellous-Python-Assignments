'''
    Q2. Print Sum of Even Numbers Between 1 and 100. Use a loop to find and print the sum of all even numbers from 1 to 100.

    Expected Output:

            Sum of even numbers between 1 to 100 is : 2550

'''

# Function Defination
def SumEven(Value):
    Sum = 0
    # Logic to Sum of even numbers between 1 to 100.
    for i in range(1, Value + 1):
        if(i % 2 == 0):             # Check Number is Even
            Sum = Sum + i
    return Sum

# Main Function
def main():

    Ret = SumEven(100)      # Function Call

    print("Sum of Even Numbers between 1 to 100 is : ", Ret)

# Starter
if __name__ == "__main__":
    main()