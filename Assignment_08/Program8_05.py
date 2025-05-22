'''
    5.Design python application which contains two threads named as thread1 and thread2.
    Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on
    screen. After execution of thread1 gets completed then schedule thread2.

    Output :

        Inside Thread1.
            1 2 3 4 5 ....... 45 46 47 48 49 50
        Inside Thread2.
            50 49 48 47 46 45 ....... 5 4 3 2 1

'''
# Import Module threading
import threading

# Function Defination.
def Thread1(Value):
    print("Inside Thread1.")

    # Logic to Display Number from 1 to 50.
    for i in range(1, Value + 1):
        print(i, end = " ")
    
    print("\n")

# Function Defination.
def Thread2(Value):
    print("Inside Thread2.")

    # Logic to Display Number from 50 to 1.
    for i in range(Value, 0, -1):
        print(i, end = " ")

    print("\n")

# Main Thread.
def main():

    # Created Thread1
    T1 = threading.Thread(target = Thread1, args = (50,))

    # Created Thread2
    T2 = threading.Thread(target = Thread2, args = (50,))

    # Start Thread1
    T1.start()

    # Wait for Thread1 completes execution.
    T1.join()

    # Start Thread2
    T2.start()

    # Wait for Thread2 completes execution.
    T2.join()

# Starter
if __name__ == "__main__":
    main()                  # Function Call.