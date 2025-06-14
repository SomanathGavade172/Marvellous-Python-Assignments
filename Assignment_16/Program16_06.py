'''
    6. Write a Python program to copy the contents of one file (source.txt) into another file (destination.txt).

'''

import os
import sys

def copy_file_content_to_another_file(source, destination):
    if not os.path.exists(source):
      print(f"{source} not exists in current directory")
      exit()

    fobj1 = open(source, 'r')
    source_data = fobj1.read()
    fobj1.close()

    fobj2 = open(destination, 'a')
    fobj2.write(source_data)    
    fobj2.close()

    print(f"{source} file data copied into {destination} successfully!")

def main():
   if (len(sys.argv) == 2):
      if(sys.argv[1] == "--h" or sys.argv[1] == sys.argv[1] == "--H"):
         print("This application is used to check the ")

      elif(sys.argv[1] == "--u" or sys.argv[1] == sys.argv[1] == "--U"):
         print("Use the given script as ")
         print("ScriptName.py FileName SourceFileName DestinationFileName")

      else:
         print("Invalid number of command line arguments")
         print("Use the given flags as :")
         print("--h: Used to display the help")
         print("--u: Used to display the usage")

   elif(len(sys.argv) == 3):
      copy_file_content_to_another_file(sys.argv[1],sys.argv[2])
   
   else:
         print("Invalid number of command line arguments")
         print("Use the given flags as :")
         print("--h: Used to display the help")
         print("--u: Used to display the usage")

if __name__ == "__main__":
    main()