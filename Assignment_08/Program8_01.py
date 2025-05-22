'''
    1. Design python application which creates two thread named as even and odd. Even thread will display first 10 even numbers and odd thread will display first 10 odd
    numbers.

    Output : 
            Even Numbers :
                            2 4 6 8 10
            Odd Numbers  :
                            1 3 5 7 9

'''
# Import Threading Module
import threading
import time

# Function Defination
def DisplayEven(No):
    print("Even Numbers : ")

    # Logic to Display Even Numbers.
    for i in range(2, No + 1, 2):
        print(i , end = " ")
    print()

# Function Defination
def DisplayOdd(No):
    print("Odd Numbers : ")

    # Logic to display Odd Numbers.
    for i in range(1, No + 1, 2):
        print(i, end = " ")
    print()

# Main Function.
def main():

    # Created Even Thread.
    T1 = threading.Thread(target = DisplayEven, args = (10,))

    # Created Odd Thread.
    T2 = threading.Thread(target = DisplayOdd, args = (10,))

    # Start Even thread.
    T1.start()
    
    # Start Odd thread.
    T2.start()
    
    # Wait for Even thread completes execution.
    T1.join()
    
    # Wait for Odd thread completes execution.
    T2.join()

# Starter.
if __name__ == "__main__":
    main()                  # Function Call.