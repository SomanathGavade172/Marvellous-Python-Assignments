'''
    4. Create a Python program that Compare execution time of summing
    numbers from 1 to 10 million using normal function, threading, and
    multiprocessing.

'''
# Import Module time, threading and multiprocessing
import time
import threading
import multiprocessing

# Function Defination
def CalculateSum(No):
    Sum = 0
    for i in range(1, No + 1):
        Sum = Sum + i

    return Sum
    
# Function Defination
def MultiThread(No):
    Sum = 0

    for i in range(1, No + 1):
        Sum = Sum + i

    print("Addition is : ", Sum)

# Function Defination
def MultiProcess(No):
    Sum = 0

    for i in range(1, No + 1):
        Sum = Sum + i

    print("Addition is : ", Sum)

# Main Function
def main():
    print("--------------------------Normal Function-------------------------")
    Start_time = time.time()

    Ret = CalculateSum(10000000)        # Function Call
    print("Addition is : ", Ret)

    End_time = time.time()
    print("Time Required for Normal Function is : ", End_time - Start_time)
    print()

    print("-----------------------Using Multithreading-----------------------")
    Start_time = time.time()

    # Created Thread
    T1 = threading.Thread(target = MultiThread, args = (10000000,))
    T1.start()      # thread start
    T1.join()       # wait for Thread execution.

    End_time = time.time()
    print("Time Required for MultiThreading is : ", End_time - Start_time)
    print()

    print("-----------------------Using Multiprocessing-----------------------")
    Start_time = time.time()

    P = multiprocessing.Process(target = MultiProcess, args = (10000000,))
    P.start()       # thread start
    P.join()        # wait for Process execution.

    End_time = time.time()
    print("Time Required for Multiprocessing is : ", End_time - Start_time)

# Starter
if __name__ == "__main__":
    main()                  # Function Call