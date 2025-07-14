'''


  * Accept input through command line or through file.
  * Display any message in log file instead of console.
  * For separate task define separate function.
  * For robustness handle every expected exception.
  * Perform validations before taking any action.
  * Create user defined modules to store the functionality.

  ---

  ## Design automation script which performs following task:

  * Accept Directory name from user and delete all duplicate files from the specified directory by considering the checksum of files.
  * Create one directory named as Marvellous and inside that directory create log file which maintains all names of duplicate files which are deleted.
  * Name of that log file should contain the date and time at which that file gets created.
  * Accept duration in minutes from user and perform task of duplicate file removal after the specific time interval.
  * Accept Mail ID from user and send the attachment of the log file.
  * Mail body should contain statistics about the operation of duplicate file removal.

  Mail body should contain below things:

  * Starting time of scanning
  * Total number of files scanned
  * Total number of duplicate files found

  ---

  ## Command line example for the script:

  text
  DuplicateFileRemoval.py E:/Data/Demo 50 marvellousinfosystem@gmail.com


  Explanation:

  * DuplicateFileRemoval.py
    Name of python automation script.

  * E:/Data/Demo
    Absolute path of directory which may contain duplicate files.

  * 50
    Time interval of script in minutes.

  * marvellousinfosystem@gmail.com
    Mail ID of the receiver.

'''
import os
import sys
import time
import schedule
import hashlib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# To calculate the checksum of file
def CalculateChecksum(path,block_size = 1024):
    fobj = open(path, 'rb')

    hobj = hashlib.md5()

    buffer = fobj.read(block_size)

    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(block_size)
        
    
    fobj.close()

    return hobj.hexdigest()

# To find duplicate files
def FindDuplicate(DirectoryName="Marvellous"):

    flag = os.path.isabs(DirectoryName)

    if (flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if(flag == False):
        print("The path is invalid")
        exit()
    
    flag = os.path.isdir(DirectoryName)

    if(flag == False):
        print("Path is valid but the target is not a directory")
        exit()
        
    Duplicate = {}
    scanned_count = 0
    start_time = time.ctime()

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):
       
        for fname in FileNames:
            fname = os.path.join(FolderName,fname)
            checksum = CalculateChecksum(fname)

            if checksum in Duplicate:
              Duplicate[checksum].append(fname) # fname is complete path
            else:
              Duplicate[checksum] = [fname]  #Adding unique files path
            
            scanned_count += 1
 
    return Duplicate,scanned_count,start_time

def DeleteDuplicate(DirectoryName="Marvellous",RecipientEmail="marvellousinfosystem@gmail.com"):
    DuplicateFileDict,ScannedFiles,ScanStartTime = FindDuplicate(DirectoryName)

    Result = list(filter(lambda x : len(x) > 1, DuplicateFileDict.values()))
    DuplicateFileCount = len(Result)
    timestamp = time.ctime()
    filename = "Delete_Duplicate%s.log" %(timestamp)
    filename = filename.replace(" ","_")
    filename = filename.replace(":","_")

    directory_name = "Marvellous"

    # To create direcory in current directory
    if not os.path.exists(directory_name):
        os.mkdir(directory_name)

    fname = os.path.join(directory_name, filename)

    obj = open(fname,'x')
    start_time = time.time()

    # To delete and store duplicate file names into log file
    for value in Result:
        for subvalue in value[1:]: #To skip first file and remove other remaining copies
          obj.write(subvalue+"\n")
          os.remove(subvalue)        

        obj.write("\n")
    
    end_time = time.time()
    obj.write("Total time required to delete duplicate files is %s seconds" %(end_time - start_time))
    obj.close()

    # To send email
    SendLogEmail(filename,RecipientEmail,ScannedFiles,DuplicateFileCount,ScanStartTime,directory_name)

def SendLogEmail(filename,recipient_email,scanned_count,duplicate_file_count,scan_start_time,directory_name):
    print("Directory name: ",directory_name)
    print("Filename: ",filename)
    print("Recipient email: ",recipient_email)
    print("Scanned count: ",scanned_count)
    print("Duplicate file count: ",duplicate_file_count)
    print("Scan start time: ",scan_start_time)

     # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login("mdubal393@gmail.com", "abcd abcd abcd abcd") #Replace your email and app password

    msg = MIMEMultipart()
    msg['From'] = "mdubal393@gmail.com"
    msg['To'] = recipient_email
    msg['Subject'] = "This is Duplicate File Deletion Log"

    line1 = f"Starting time of scanning: {scan_start_time}"
    line2 = f"Total number of files scanned: {scanned_count}"
    line3 = f"Total number of duplicate files found: {duplicate_file_count}"

    body = f"{line1}\n\n{line2}\n\n{line3}"

    # Attach the body
    msg.attach(MIMEText(body, 'plain'))

    fname = os.path.join(directory_name, filename)

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


def main():
    if (len(sys.argv) == 2):
      if(sys.argv[1] == "--h" or sys.argv[1] == sys.argv[1] == "--H"):
          print("This application is used to perform directory cleaning")
          print("This is the directory automation script")

      elif(sys.argv[1] == "--u" or sys.argv[1] == sys.argv[1] == "--U"):
          print("Use the given script as ")
          print("ScriptName.py NameOfDirectory TimeInterval RecipientEmail")
          print("Please provide valid absolute path")
  
    if (len(sys.argv) == 4):

      def job():
        DeleteDuplicate(sys.argv[1], sys.argv[3])

      schedule.every(int(sys.argv[2])).minutes.do(job)


      while True:
          schedule.run_pending()
          time.sleep(1)
    
    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as :")
        print("--h: Used to display the help")
        print("--u: Used to display the usage")


if __name__ == "__main__":
    main()