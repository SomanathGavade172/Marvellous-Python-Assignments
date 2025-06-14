'''
    5. Write a program to read a file line by line and display only those lines that contain more than 5 words.

'''
import sys
import os

def print_specific_lines(filename):
    if not os.path.exists(filename):
        print(f"{filename} does not exist in the current directory.")
        exit()

    with open(filename) as fobj:
        
        for line in fobj:
            words = line.split()

            if (len(words) >= 5):
                print(line)
        
def main():
    if (len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == sys.argv[1] == "--H"):
            print("This application is used to take 10 numbers from user and save them into file")

        elif(sys.argv[1] == "--u" or sys.argv[1] == sys.argv[1] == "--U"):
            print("Use the given script as ")
            print("ScriptName.py FileName")

        else:
            print_specific_lines(sys.argv[1])

    else:
      print("Invalid number of command line arguments")
      print("Use the given flags as :")
      print("--h: Used to display the help")
      print("--u: Used to display the usage")

if __name__ == "__main__":
    main()