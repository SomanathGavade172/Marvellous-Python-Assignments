'''
   4. Design automation script which accept two directory names and one file extension. Copy all files with the specified extension from first directory into second directory. Second directory
   should be created at run time.
   Usage : DirectoryCopyExt.py “Demo” “Temp” “.exe”
   Demo is name of directory which is existing and contains files in it. We have to create new
   Directory as Temp and copy all files with extension .exe from Demo to Temp.

'''

import os
import sys
import shutil

def copy_files_into_new_directory(source_directory,new_directory,file_extension):

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

   # To copy all files with given extension into new directory 
   for FolderName, SubFolderNames, FileNames in os.walk(source_directory):
      
      # Build the path relative to the source directory
      relative_path = os.path.relpath(FolderName, source_directory)
      destination_path = os.path.join(new_directory, relative_path)

      # To create the subfolder in the destination if it doesn't exist
      if not os.path.exists(destination_path):
         os.mkdir(destination_path)

      for fname in FileNames:
         if fname.endswith(file_extension):
            source_file = os.path.join(FolderName, fname)
            destination_file = os.path.join(destination_path, fname)

            shutil.copy(source_file, destination_file)

   print(f"\nAll files with {file_extension} copied successfully into {new_directory}")

def main():
   if (len(sys.argv) == 2):
      if(sys.argv[1] == "--h" or sys.argv[1] == sys.argv[1] == "--H"):
         print("This application is used to copy all files of given extension from existing directory into new directory.")

      elif(sys.argv[1] == "--u" or sys.argv[1] == sys.argv[1] == "--U"):
         print("Use the given script as ")
         print("ScriptName.py OldDirectoryName NewDirectoryName FileExtension")

      else:
         print("Invalid number of command line arguments")
         print("Use the given flags as :")
         print("--h: Used to display the help")
         print("--u: Used to display the usage")

   elif(len(sys.argv) == 4 ):
      copy_files_into_new_directory(sys.argv[1],sys.argv[2],sys.argv[3])
   
   else:
         print("Invalid number of command line arguments")
         print("Use the given flags as :")
         print("--h: Used to display the help")
         print("--u: Used to display the usage")

if __name__ == "__main__":
   main()
