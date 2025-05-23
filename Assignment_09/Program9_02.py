'''
    2. Write a Python program using multiprocessing.Process to square a list of numbers using multiple processes.

    Input  : 
            Enter Number of Elements :  5
                    Enter 5 Numbers  :  1  2  3  4  5 
    Output :                            
        Square of List of Numbers is :  [1, 4, 9, 16, 25]
'''

# Import Module 
import multiprocessing

# Function Defination
def Square(Values):
    SList = []      # Empty List

    # Logic to Calculate Square.
    for i in Values:
        # Square = lambda X : X ** 2
        Square = i ** 2
        SList.append(Square)

    print("Square of List of Numbers is : ", SList)

# Main Function
def main():
    List = []       # Empty List

    print("Enter Number of Elements : ")

    # Accept Input Integer.
    try:
        Size = int(input())
    
    except(ValueError):
        print("Invalid Input..! Enter Numeric Values..!")
        return
    
    print("Enter", Size , "Numbers : ")

    # Accept Integer Input    
    try:
        # Accept Numbers form User.
        for i in range(Size):
            No = int(input())

            List.append(No)         # Append Numbers into a List.

    except(ValueError):
        print("Invalid Input..! Enter Numeric Values..!")
        return
    
    # Created Process
    P = multiprocessing.Process(target = Square, args = (List,))

    # Process Start
    P.start()

    # wait forProcess Execution 
    P.join()

# Starter
if __name__ == "__main__":
    main()                  # Function Call