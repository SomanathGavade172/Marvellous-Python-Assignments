'''
    3. Write a program that schedules a function to print “Do Coding..!” every 30 minutes.
'''

import schedule
import time

def print_function():
    print("Do Coding..!")

def main():
    schedule.every(30).minutes.do(print_function)

    while True:
        schedule.run_pending
        time.sleep(1)
if __name__ == "__main__":
    main()