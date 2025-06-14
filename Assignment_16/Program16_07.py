'''
    7. Create a file marks.txt with student name and marks. Then read the file and display students who scored more than 75 marks.

'''
import os
import sys

def print_students(filename):
    if not os.path.exists(filename):
        print(f"{filename} file does not exists in current directory.")
    
    with open(filename) as fobj:
        file_contents = fobj.read().splitlines()
        # print(file_contents)
    
    for line, row in enumerate(file_contents):
        col = row.split(" ")
        if(int(col[1]) > 75):
            print(row)

def main():
    if (len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == sys.argv[1] == "--H"):
            print("This application is used to print students with marks more than 75")

        elif(sys.argv[1] == "--u" or sys.argv[1] == sys.argv[1] == "--U"):
            print("Use the given script as ")
            print("ScriptName.py FileName")

        else:
            print_students(sys.argv[1])

    else:
      print("Invalid number of command line arguments")
      print("Use the given flags as :")
      print("--h: Used to display the help")
      print("--u: Used to display the usage")

if __name__ == "__main__":
    main()