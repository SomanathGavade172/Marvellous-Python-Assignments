'''
    4. Design automation script which accept directory name and delete all duplicate files from that directory. Write names of duplicate files from that directory into log file named as Log.txt.
    Log.txt file should be created into current directory. Display execution time required for the script.
    Usage : DirectoryDusplicateRemoval.py “Demo”
    Demo is name of directory.

'''

import os
import sys
import hashlib
import time

def CalculateChecksum(path,block_size = 1024):
    fobj = open(path, 'rb')

    hobj = hashlib.md5()

    buffer = fobj.read(block_size)

    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(block_size)
    
    fobj.close()

    return hobj.hexdigest()

def duplicate_files(directory_name):
       
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

    Duplicate = {}

    for FolderName, SubFolderNames, FileNames in os.walk(directory_name):

        for fname in FileNames: 
            path = os.path.join(FolderName,fname)
            checksum = CalculateChecksum(path)

            if checksum in Duplicate:
                Duplicate[checksum].append(path) # fname is complete path
            else:
                Duplicate[checksum] = [path]  #Adding unique files path

    return Duplicate

def delete_duplicate_files(duplicate_files):
    Result = list(filter(lambda x : len(x) > 1, duplicate_files.values()))

    timestamp = time.ctime()
    filename = "Delete_Duplicate_with_time_%s.log" %(timestamp)
    filename = filename.replace(" ","_")
    filename = filename.replace(":","_")

    obj = open(filename,'x')
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

def main():
    if (len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == sys.argv[1] == "--H"):
            print("This application is used to display the files with given extension")

        elif(sys.argv[1] == "--u" or sys.argv[1] == sys.argv[1] == "--U"):
            print("Use the given script as ")
            print("ScriptName.py DirectorytName")

        else:
            duplicateFiles =duplicate_files(sys.argv[1])
            delete_duplicate_files(duplicateFiles)

    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as :")
        print("--h: Used to display the help")
        print("--u: Used to display the usage")

if __name__ == "__main__":
    main()