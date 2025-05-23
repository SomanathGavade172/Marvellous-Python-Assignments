'''
    3. Create a Python program that uses multiprocessing.Pool to compute factorial of numbers in a list.

'''
# Import Module
import multiprocessing

# Function Defination.
def Factorial(Values):
    Fact = 1

    # Logic Calculate of Factorial
    for i in range(1, Values + 1):
        Fact = Fact * i

    return Fact

# Main Function
def main():
    List = []       # Empty List

    # Accept Number of Element from User.
    print("Enter Number of Elements : ")

    # Accept Integer Input
    try:
        Size = int(input())

    except(ValueError):
        print("Invalid Input..! Enter Numeric Values..!")
        return
    
    print("Enter", Size, "Numbers : ")

    # Accept Integer Input
    try:
        # Accept Numbers form User.
        for i in range(Size):
            No = int(input())

            # Factorial of -ve Number Can not Calculate
            if (No < 0):
                print("Factorial is not defined for negative numbers!")
                return
            
            List.append(No)     # Append Numbers into a List.

    except(ValueError):
        print("Invalid Input..! Enter Numeric Values..!")
        return
    
    # Created Process
    P = multiprocessing.Pool()

    # Multiple Process calculate Factorial
    Ret = P.map(Factorial, List)

    print("Factorial of Numbers in a list is : ", Ret)

# Starter
if __name__ == "__main__":
    main()                  # Function Call