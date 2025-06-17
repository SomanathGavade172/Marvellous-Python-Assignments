'''
    8. Write a script that simulates checking for email updates every 10 seconds. (Use a print statement like “Checking mail...” instead of real email logic.)

'''

import time
import schedule
import datetime

def file_backup():

    # Copy the file contents of main file into backup file
    fobj1 = open("Demo.txt", 'r')  #Original file to take backup
    data = fobj1.read()

    timestamp = datetime.datetime.now().strftime('%Y__%m__%d %H_%M_%S')
    timestamp = timestamp.replace(" ","____")

    backup_file = "Backup%s.log" %(timestamp)

    fobj2 = open(backup_file, 'x')
    fobj2.write(data)

    # Append the time log when backup is taken

    fobj_log = open("backup_log.txt", 'a')
    fobj_log.write(f"File backup completed sucessfully at {timestamp}\n")

def main():
    # schedule.every().hour.do(file_backup)
    schedule.every(5).seconds.do(file_backup)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()