'''
    5. Schedule a job that runs every 5 minutes to write the current time to a file Marvellous.txt.
'''

import time 
import schedule
import datetime

def log_time_to_file():

    fobj = open("Marvellous.txt","a")
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    fobj.write(f"{current_time}\n")
    fobj.close()
    print("Time added successfully!")

def main():
    schedule.every(5).minutes.do(log_time_to_file)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()