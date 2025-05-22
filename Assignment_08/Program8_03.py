'''
    3. Design python application which creates two threads as evenlist and oddlist. Both the threads accept list of integers as parameter. Evenlist thread add all even elements
    from input list and display the addition. Oddlist thread add all odd elements from input list and display the addition.

    Input  :
        Enter Number of Elements : 10
        Enter 10 Numbers         : 11 12 13 14 15 16 17 18 19 20

    Output :
        Even List is :  [12, 14, 16, 18, 20]
        Addition is  :  80

        Odd List is  :  [11, 13, 15, 17, 19]
        Addition is  :  75

'''
# Import Module threading
import threading

# Function Defination
def EvenList(Values):
    EList = []          # Empty List.
    Sum = 0

    # Logic to addition of Even numbers.
    for i in range(len(Values)):
        # logic to Check Value is Even and Sum.
        if(Values[i] % 2 == 0):
            EList.append(Values[i])
            Sum = Sum + Values[i]
            
    print("Even List is : ", EList)
    print("Sum of all Even Numbers is : ", Sum)

# Function Defination
def OddList(Values):
    OList = []      # Empty List
    Sum = 0

    # Logic to addition of Odd numbers.
    for i in range(len(Values)):
        # logic to Check Value is Odd and Sum.
        if(Values[i] % 2 != 0):
            OList.append(Values[i])
            Sum = Sum + Values[i]

    print("Odd List is : ", OList)
    print("Sum of all Odd Numbers is : ", Sum)

# Main Function
def main():
    List = []       # Empty List

    # Accept number Elements from User.
    print("Enter Number of Elements : ")

    # Accept Integer Numbers.
    try:
        # Input Size of List.
        Size = int(input())

    except(ValueError):
        print("Invalid Input..! Enter Numeric Values..!")
        return
    
    print("Enter", Size, "Numbers : ")

    # Accept Integer Numbers.
    try:
        # Accept Numbers from User.
        for i in range(Size):
            No = int(input())
            List.append(No)
    except(ValueError):
        print("Invalid Input..! Enter Numeric Values..!")
        return
    
    # Created Thread EvenList
    T1 = threading.Thread(target = EvenList, args = (List,))

    # Created Thread OddList
    T2 = threading.Thread(target = OddList, args = (List,))

    # Start EvenList Thread
    T1.start()

    # Start OddList Thread
    T2.start()

    # Wait for EvenList thread completes execution.
    T1.join()

    # Wait for OddList thread completes execution.
    T2.join()

# Starter
if __name__ == "__main__":
    main()                  # Function Call.
