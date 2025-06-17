'''
   2. Write a program which accept file name from user and open that file and display the contents of that file on screen.
   
   Input : Demo.txt
   Display contents of Demo.txt on console.

'''

import os

def display_file_contains(filename):
   if not os.path.exists(filename):
      print(f"{filename} not exists in the current directory.")
      exit()

   fobj = open(filename, 'r')

   data = fobj.read()

   print(data)

   fobj.close()

def main():
   fname = input("Enter name of the file:  ")
   display_file_contains(fname)
   
if __name__ == "__main__":
   main()

