'''
    2. Design python application which creates two threads as evenfactor and oddfactor.Both the thread accept one parameter as integer. Evenfactor thread will display
    addition of even factors of given number and oddfactor will display addition of odd factors of given number. After execution of both the thread gets completed main
    thread should display message as “exit from main”.

    Input  :
        Enter a Number :
                            6
    Output :
        Addition of Even Factors is :  8
        Addition of Odd Factors is  :  4
        Exits From Main.

    Input :
        Enter a Number :
                            13
    Output :
        Addition of Even Factors is :  0
        Addition of Odd Factors is  :  14
        Exits From Main.
'''

# Import Module threading.
import threading

# Function Defination
def EvenFactor(Value):
    Sum = 0
    
    # Logic to Calculate Sum of Even Factors.
    for i in range(2 , (Value // 2) + 1, 2):
        if(Value % i == 0):
            Sum = Sum + i
    
    # Logic to check given number is Divisible by 2 & add to Sum. 
    if(Value % 2 == 0):
        Sum = Sum + Value
    print("Addition of Even Factors is : ", Sum)

# Function Defination
def OddFactor(Value):
    Sum = 0

    # Logic to Calculate Sum of Odd Factors.
    for i in range(1, (Value // 2) + 1, 2):
        if(Value % i == 0):
            Sum = Sum + i
    # Logic to check given number is Not Divisible by 2 & add to Sum. 
    if(Value % 2 != 0):
        Sum = Sum + Value
    print("Addition of Odd Factors is : ", Sum)

# Main Function
def main():
    print("Enter a Number : ")

    # Accept Integer Numbers Only.
    try:
        # accept Number from User
        No = int(input())

    except(ValueError):
        print("Invalid Input..! Enter Numeric Values..!")
        return 

    # Created EvenFactor Thread.
    T1 = threading.Thread(target = EvenFactor, args = (No,))

    # Created OddFactor Thread.
    T2 = threading.Thread(target = OddFactor, args = (No,))

    # start EvenFactor Thread.
    T1.start()

    # start OddFactor Thread.
    T2.start()

    # Wait for EvenFactor thread completes execution.
    T1.join()

    # Wait for OddFactor thread completes execution.
    T2.join()

    print("Exits From Main.")

# starter
if __name__ == "__main__":
    main()                  # Function Call