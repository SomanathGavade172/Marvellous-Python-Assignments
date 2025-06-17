'''
   5. Accept file name and one string from user and return the frequency of that string from file.

   Input : Demo.txt Marvellous
   Search “Marvellous” in Demo.txt

'''

import os
import sys

def search_string_frequency(filename,str):
   if not os.path.exists(filename):
      print(f"{filename} not exists in current directory")
      exit()
   
   fobj = open(filename, 'r')
   data = fobj.read()

   count = data.count(str)

   fobj.close()
   
   return count

def main():
   if (len(sys.argv) == 2):
      if(sys.argv[1] == "--h" or sys.argv[1] == sys.argv[1] == "--H"):
         print("This application is used to check the ")

      elif(sys.argv[1] == "--u" or sys.argv[1] == sys.argv[1] == "--U"):
         print("Use the given script as ")
         print("ScriptName.py FileName StringName")

      else:
         print("Invalid number of command line arguments")
         print("Use the given flags as :")
         print("--h: Used to display the help")
         print("--u: Used to display the usage")

   elif(len(sys.argv) == 3):
      ret = search_string_frequency(sys.argv[1],sys.argv[2])

      print(f"Frequency of {sys.argv[2]} in {sys.argv[1]} file is : ",ret)
   
   else:
         print("Invalid number of command line arguments")
         print("Use the given flags as :")
         print("--h: Used to display the help")
         print("--u: Used to display the usage")

if __name__ == "__main__":
   main()