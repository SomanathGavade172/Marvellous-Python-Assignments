'''
    4. Accept 10 numbers from the user and write them into a file named numbers.txt, each on a new line.

'''

import sys

def add_numbers_to_file(filename):

    fobj = open(filename,'w')

    print("Enter 10 numbers: ")
    for i in range(10):
        num = int(input())
        fobj.write(str(num)+"\n") 
    
    print("Numbers added successfully!")

    fobj.close()

def main():
    if (len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == sys.argv[1] == "--H"):
            print("This application is used to take 10 numbers from user and save them into file")

        elif(sys.argv[1] == "--u" or sys.argv[1] == sys.argv[1] == "--U"):
            print("Use the given script as ")
            print("ScriptName.py FileName")

        else:
            add_numbers_to_file(sys.argv[1])

    else:
      print("Invalid number of command line arguments")
      print("Use the given flags as :")
      print("--h: Used to display the help")
      print("--u: Used to display the usage")

if __name__ == "__main__":
    main()