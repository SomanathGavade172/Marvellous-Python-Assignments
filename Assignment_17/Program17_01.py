'''
    1. Write a Python script that prints “Jay Ganesh...” every 2 seconds. Use the schedule.every(2).seconds.do(...) function.

'''

import schedule
import time

def print_function():
    print("Jay Ganesh...")

def main():
    schedule.every(2).seconds.do(print_function)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()