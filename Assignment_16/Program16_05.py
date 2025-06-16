'''
    5. Write a program to read a file line by line and display only those lines that contain more than 5 words.

'''
# Import Module os and sys
import os
import sys

# Function Defination
def DisplayLine(FName):
    
    # Check File is Precent in the Current Directory
    bRet = os.path.exists(FName)

    if(bRet == False):
        print("File is not Present in the Current Directory")
        exit()

    # Open the File into Read Mode
    fobj = open(FName, "r")

    # read the Data into the File.
    Data = fobj.readlines()

    # Logic to Check Line conations More than 5 words.
    for Line in Data:
        Word = Line.split()

        if(len(Word) >= 5):
            print(Line.strip())     # strip() - Used to remove lines.

    # File is Close    
    fobj.close()

# Main Function
def main():
    if(len(sys.argv) == 2):
        if((sys.argv[1] == '--h') or (sys.argv[1] == '--H')):
            print("This Application is used to Display only those lines from file which contain more than 5 words.")
        
        elif((sys.argv[1] == '--u') or (sys.argv[1] == '--H')):
            print("Use the given scripts as :")
            print("python ScriptName.py FileName")

        else:
            DisplayLine(sys.argv[1])        # Function Call
    
    else:
        print("Invalid Number of Command Line Arguments.")
        print("Use the given Flags as : ")
        print("--h : used to Display the Help")
        print("--u : used to Display the Usage")

# Starter
if __name__ == "__main__":
    main()                  # Function Call
