'''
    1. Create a Python program that starts 3 threads, each printing numbers from 1 to 5 with a delay of 1 second. Use threading.Thread.

    Output : 
            Inside Thread 1.
            1 2 3 4 5

            Inside Thread 2.
            1 2 3 4 5

            Inside Thread 3.
            1 2 3 4 5
'''
# Import Module threading
import threading
# Import Module time
import time

# Function Defination.
def  Thread1(Value, delay = 1,):
    print("Inside Thread 1.")

    # Ligic to Display Number from 1 to 5.
    for i in range(1, Value + 1):
        print(i , end = " ")
        time.sleep(delay)       # delay 1 second after printing.

    print("\n")

# Function Defination.
def Thread2(Value, delay = 1):
    print("Inside Thread 2.")

    # Ligic to Display Number from 1 to 5.
    for i in range(1, Value + 1):
        print(i, end = " ")
        time.sleep(delay)       # delay 1 second after printing.
    
    print("\n")

# Function Defination.
def  Thread3(Value, delay = 1):
    print("Inside Thread 3.")

    # Ligic to Display Number from 1 to 5.
    for i in range(1, Value + 1):
        print(i, end = " ")
        time.sleep(delay)       # delay 1 second after printing.

    print("\n")

# Main Function.
def main():
    # Created Thread1.
    T1 = threading.Thread(target = Thread1, args = (5,))
    T1.start()      # Start Thread1 
    T1.join()       # wait for Thread1 execution.

    # Created Thread2.
    T2 = threading.Thread(target = Thread2, args = (5,))
    T2.start()      # Start Thread1 
    T2.join()       # wait for Thread1 execution.

    # Created Thread3.
    T3 = threading.Thread(target = Thread3, args = (5,))
    T3.start()      # Start Thread1 
    T3.join()       # wait for Thread1 execution.

    print("End of Main.")
    
# Main Function
if __name__ == "__main__":
    main()                  # Function 