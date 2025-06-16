'''
    4. Accept 10 numbers from the user and write them into a file Named numbers.txt, each on a new line.

'''
# Import Module os and sys
import os
import sys

# Function Defination
def WriteNumbers(FName):

    # Open the File into Write Mode.
    fobj = open(FName, "w")

    print("Enter 10 Numbers : ")

    # Accept 10 Numbers from the User.
    for i in range(10):
        iNo = int(input())

        # Write 10 numbers into the File
        fobj.write(str(iNo) + "\n")

    # File is Close
    fobj.close()

    print("Number Added Successfully into the File")

# Main Function
def main():

    if(len(sys.argv) == 2):
        if((sys.argv[1] == '--h') or (sys.argv[1] == '--H')):
            print("This application accepts 10 numbers from user and writes them into a file, one per line.")
        
        elif((sys.argv[1] == '--u') or (sys.argv[1] == '--H')):
            print("Use the given scripts as :")
            print("python ScriptName.py FileName")

        else:
            WriteNumbers(sys.argv[1])        # Function Call
    
    else:
        print("Invalid Number of Command Line Arguments.")
        print("Use the given Flags as : ")
        print("--h : used to Display the Help")
        print("--u : used to Display the Usage")

# Starter
if __name__ == "__main__":
    main()                  # Function Call.
