'''
   1.Design automation script which accept directory name and file extension from user. Display all files with that extension.
   Usage : DirectoryFileSearch.py “Demo” “.txt”
   Demo is name of directory and .txt is the extension that we want to search.

'''

import os
import sys

def display_files(directory_name, extension): 
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

   # To display files with given extension
   for FolderName, SubFolderNames, FileNames in os.walk(directory_name):
        for fname in FileNames:
            if fname.endswith(extension): #To check file with given extension
               # print(fname)
               log_file = os.path.basename(__file__)
               log_file = log_file.replace(".py",".log")

               with open(log_file, 'a') as fobj:
                  fobj.write(f"{fname}\n")

def main():
   if (len(sys.argv) == 2):
      if(sys.argv[1] == "--h" or sys.argv[1] == sys.argv[1] == "--H"):
         print("This application is used to display the files with given extension")

      elif(sys.argv[1] == "--u" or sys.argv[1] == sys.argv[1] == "--U"):
         print("Use the given script as ")
         print("ScriptName.py DirectortName FIleExtension")

      else:
         print("Invalid number of command line arguments")
         print("Use the given flags as :")
         print("--h: Used to display the help")
         print("--u: Used to display the usage")

   elif(len(sys.argv) == 3):
      display_files(sys.argv[1],sys.argv[2])
   
   else:
         print("Invalid number of command line arguments")
         print("Use the given flags as :")
         print("--h: Used to display the help")
         print("--u: Used to display the usage")

if __name__ == "__main__":
   main()

