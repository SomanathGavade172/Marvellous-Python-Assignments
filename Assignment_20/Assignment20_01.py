'''
    1.Design automation script which accept directory name and display checksum of all files.
    Usage : DirectoryChecksum.py “Demo”
    Demo is name of directory.

'''

import hashlib
import os
import sys

def display_checksum(directory_name):
       
    # Check if directory is valid or not
    flag = os.path.isabs(directory_name)
    if (flag == False):
        directory_name = os.path.abspath(directory_name)

    flag = os.path.exists(directory_name)

    if(flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(directory_name)

    if(flag == False):
        print("Path is valid but the target is not a directory")
        exit()

    for FolderName, SubFolderNames, FileNames in os.walk(directory_name):

        for fname in FileNames: 
            path = os.path.join(FolderName,fname)
            fobj = open(path, 'rb')

            hobj = hashlib.md5()

            buffer = fobj.read(1024)

            while(len(buffer) > 0):
                hobj.update(buffer)
                buffer = fobj.read(1024)
                
            fobj.close()

            print(f"Checksum of{fname} file is : {hobj.hexdigest()}")

def main():
   if (len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == sys.argv[1] == "--H"):
            print("This application is used to display the files with given extension")

        elif(sys.argv[1] == "--u" or sys.argv[1] == sys.argv[1] == "--U"):
            print("Use the given script as ")
            print("ScriptName.py DirectorytName")

        else:
            display_checksum(sys.argv[1]) 

   else:
        print("Invalid number of command line arguments")
        print("Use the given flags as :")
        print("--h: Used to display the help")
        print("--u: Used to display the usage")

if __name__ == "__main__":
    main()