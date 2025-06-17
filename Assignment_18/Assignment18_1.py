'''
   1. Write a program which accepts file name from user and check whether that file exists in current directory or not.

   Input : Demo.txt
   Check whether Demo.txt exists or not.

'''

import os

def check_file_exists(filename):

   return (os.path.exists(filename))

def main():

   fname = input("Enter name of the file: ")
   ret = check_file_exists(fname)

   if(ret == True):
      print(f"{fname} file exists in the current directory.")
   else:
      print(f"{fname} file does not exists in the current directory.")

if __name__ == "__main__":
   main()

