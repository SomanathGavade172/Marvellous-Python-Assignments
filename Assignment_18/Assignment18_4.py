'''
   4. Write a program which accept two file names from user and compare contents of both the files. If both the files contains same contents then display success otherwise display failure.
   Accept names of both the files from command line.

   Input : Demo.txt Hello.txt
   Compare contents of Demo.txt and Hello.txt
'''

import os
import sys

def check_file_contents(file1, file2):
   if not os.path.exists(file1):
      print(f"{file1} not exists in current directory")
      exit()
   
   if not os.path.exists(file2):
      print(f"{file2} not exists in current directory") 
      exit()
   
   fobj1 = open(file1, 'r')
   file1_data = fobj1.read()

   fobj2 = open(file2, 'r')
   file2_data = fobj2.read()

   fobj1.close()
   fobj2.close()

   return (file1_data == file2_data)   

def main():
   if (len(sys.argv) == 2):
      if(sys.argv[1] == "--h" or sys.argv[1] == sys.argv[1] == "--H"):
         print("This application is used to check the ")

      elif(sys.argv[1] == "--u" or sys.argv[1] == sys.argv[1] == "--U"):
         print("Use the given script as ")
         print("ScriptName.py FirstFileName SecondFileName")

      else:
         print("Invalid number of command line arguments")
         print("Use the given flags as :")
         print("--h: Used to display the help")
         print("--u: Used to display the usage")

   elif(len(sys.argv) == 3):
      ret = check_file_contents(sys.argv[1],sys.argv[2])

      if ret == True:
         print(f"Success")
      else:
         print("Failure")
   
   else:
         print("Invalid number of command line arguments")
         print("Use the given flags as :")
         print("--h: Used to display the help")
         print("--u: Used to display the usage")

if __name__ == "__main__":
   main()