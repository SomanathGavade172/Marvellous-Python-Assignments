'''
   2. Design automation script which accept directory name and two file extensions from user.Rename all files with first file extension with the second file extenntion.
   Usage : DirectoryRename.py “Demo” “.txt” “.doc”
   Demo is name of directory and .txt is the extension that we want to search and rename
   with .doc.
   After execution this script each .txt file gets renamed as .doc.

'''

import os
import sys

def rename_file_extension(directory_name, old_extension, new_extension):
   print("inside rename_file_extension")
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

   # To rename files with given extension
   for FolderName, SubFolderNames, FileNames in os.walk(directory_name):
        print(FolderName)
        for fname in FileNames:
            if fname.endswith(old_extension):
               print(fname)
               log_file = os.path.basename(__file__)
               log_file = log_file.replace(".py",".log")
               pre, ext = os.path.splitext(fname)
              
               print(pre + new_extension)
               fpath = os.path.abspath(directory_name)+"/"+fname
               os.rename(fpath, os.path.join(FolderName, pre + new_extension))

               with open(log_file, 'a') as fobj:
                  fobj.write(f"Old name: {fname} ___ New name: { pre + new_extension}\n")

def main():
   print("inside main")
   if (len(sys.argv) == 2):
      if(sys.argv[1] == "--h" or sys.argv[1] == sys.argv[1] == "--H"):
         print("This application is used to rename the files extension with given extension")

      elif(sys.argv[1] == "--u" or sys.argv[1] == sys.argv[1] == "--U"):
         print("Use the given script as ")
         print("ScriptName.py DirectortName ExtensionToSearch FileExtensionToRenameWith")

      else:
         print("Invalid number of command line arguments")
         print("Use the given flags as :")
         print("--h: Used to display the help")
         print("--u: Used to display the usage")

   elif(len(sys.argv) == 4 ):
      rename_file_extension(sys.argv[1],sys.argv[2],sys.argv[3])
   
   else:
         print("Invalid number of command line arguments")
         print("Use the given flags as :")
         print("--h: Used to display the help")
         print("--u: Used to display the usage")

if __name__ == "__main__":
   main()

