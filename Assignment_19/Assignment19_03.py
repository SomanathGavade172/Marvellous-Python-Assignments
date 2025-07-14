'''
   3. Design automation script which accept two directory names. Copy all files from first directory into second directory. Second directory should be created at run time.
   Usage : DirectoryCopy.py “Demo” “Temp”
   Demo is name of directory which is existing and contains files in it. We have to create new
   Directory as Temp and copy all files from Demo to Temp.
'''

import os
import sys
import shutil

def copy_files_into_new_directory(source_directory,new_directory):

   # Check if directory is valid or not
   flag = os.path.isabs(source_directory)
   if (flag == False):
      source_directory = os.path.abspath(source_directory)

   flag = os.path.exists(source_directory)

   if(flag == False):
      print("The path is invalid")
      exit()

   flag = os.path.isdir(source_directory)

   if(flag == False):
      print("Path is valid but the target is not a directory")
      exit()

   # To create new directory if it doesn't exist
   if not os.path.exists(new_directory):
      os.mkdir(new_directory)
   else:
      print(f"{new_directory} already exists!")
      exit()

   # To copy all files into new directory 
   for FolderName, SubFolderNames, FileNames in os.walk(source_directory):
      
      # To build the path relative to the source directory
      relative_path = os.path.relpath(FolderName, source_directory)
      # print("Relative Path: ", relative_path)
      destination_path = os.path.join(new_directory, relative_path)
      # print("Destination Path: ", destination_path)

      # To create the subfolder in the destination if it doesn't exist
      if not os.path.exists(destination_path):
         os.mkdir(destination_path)

      for fname in FileNames:
         source_file = os.path.join(FolderName, fname)
         destination_file = os.path.join(destination_path, fname)

         shutil.copy(source_file, destination_file)

   print(f"\nAll files copied successfully into {new_directory}")

def main():
   if (len(sys.argv) == 2):
      if(sys.argv[1] == "--h" or sys.argv[1] == sys.argv[1] == "--H"):
         print("This application is used to copy all files from first directory into second directory.")

      elif(sys.argv[1] == "--u" or sys.argv[1] == sys.argv[1] == "--U"):
         print("Use the given script as ")
         print("ScriptName.py OldDirectoryName NewDirectoryName")

      else:
         print("Invalid number of command line arguments")
         print("Use the given flags as :")
         print("--h: Used to display the help")
         print("--u: Used to display the usage")

   elif(len(sys.argv) == 3 ):
      copy_files_into_new_directory(sys.argv[1],sys.argv[2])
   
   else:
         print("Invalid number of command line arguments")
         print("Use the given flags as :")
         print("--h: Used to display the help")
         print("--u: Used to display the usage")

if __name__ == "__main__":
   main()


