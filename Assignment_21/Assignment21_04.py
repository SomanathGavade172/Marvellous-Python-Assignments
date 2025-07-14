'''
    4. Design automation script which accept directory name and mail id from user and create log file in that directory which contains information of running processes as its name, PID,
    Username. After creating log file send that log file to the specified mail.
    Usage : ProcInfoLog.py Demo Marvellousinfosystem@gmail.com
    Demo is name of Directory.
    marvellousinfosystem@gmail.com is the mail id.

'''


import sys
import psutil
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def SendLogEmail(directory_name, recipient_email):
    
# Logic to add current running process information to a log file
    ProcessInfo = []
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=['pid', 'name', 'username'])
        info['vms'] = proc.memory_info().vms / (1024 * 10124)
        print(info)
        ProcessInfo.append(str(info)+"\n")
    
    timestamp = time.ctime()
    filename = "Process_%s.log" %(timestamp)
    filename = filename.replace(" ","_")
    filename = filename.replace(":","_") 

    # To create direcory in current directory
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)
    else:
        print(f"{directory_name} already exists!")
        exit()
    
    fname = os.path.join(directory_name, filename)

    with open(fname, "w") as obj:
        for info in ProcessInfo:
            obj.write(str(info)+ "\n")
    print(f"Log file '{fname}' created in the current directory.")

# --------------------------Logic to send email---------------------------------
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login("mdubal393@gmail.com", "abcd abcd abcd abcd") #Replace your email and app password

    msg = MIMEMultipart()
    msg['From'] = "mdubal393@gmail.com"
    msg['To'] = recipient_email
    msg['Subject'] = "This is Process Information Log message"

    attachment = open(fname, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename= {filename}')

    msg.attach(part)

    # sending the mail
    s.sendmail("mdubal393@gmail.com", recipient_email, msg.as_string())

    # terminating the session
    s.quit()
# ------------------------------------------------------------------------------

def main():
    if (len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == sys.argv[1] == "--H"):
            print("This application is used to display the files with given extension")

        elif(sys.argv[1] == "--u" or sys.argv[1] == sys.argv[1] == "--U"):
            print("Use the given script as ")
            print("ScriptName.py ProcessName RecipientEmail")

        else:
            print("Invalid number of command line arguments")
            print("Use the given flags as :")
            print("--h: Used to display the help")
            print("--u: Used to display the usage")

    elif (len(sys.argv) == 3):
        SendLogEmail(sys.argv[1],sys.argv[2])

    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as :")
        print("--h: Used to display the help")
        print("--u: Used to display the usage")

if __name__ == "__main__":
    main()