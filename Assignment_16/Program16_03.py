'''
    3. Write a Python script to count the number of lines, words, and characters in a given file.

'''
# Import Module os & sys
import os
import sys

# Function Defination
def DisplayFileInfo(FName):

    # Check File is Precent in the Current Directory 
    bRet = os.path.exists(FName)

    if(bRet == False):
        print("File is not Present in the Current Directory..!")
        exit

    # Open the Filoe into Read Mode.
    fobj = open(FName, "r")

    # Read the Data into the File
    Data = fobj.read()

    # Logic to Count Number of Lines.
    Lines = Data.splitlines()
    print("Number of Lines Present into the File is : ", len(Lines))

    # Logic to Count Number of Words.
    words = Data.split()
    print("Number of Words Present into the File is : ", len(words))

    # Logic to Count Number of Characters.
    Characters = len(Data)
    print("Number of Characters Present into the File is : ", Characters)

    # Close the File.
    fobj.close()

# Main Function
def main():
    
    if(len(sys.argv) == 2):
        if((sys.argv[1] == '--h') or (sys.argv[1] == '--H')):
            print("This Application is used to Count Number of Lines, World & Characters.")
        
        elif((sys.argv[1] == '--u') or (sys.argv[1] == '--H')):
            print("Use the given scripts as :")
            print("python ScriptName.py FileName")

        else:
            DisplayFileInfo(sys.argv[1])        # Function Call
    
    else:
        print("Invalid Number of Command Line Arguments.")
        print("Use the given Flags as : ")
        print("--h : used to Display the Help")
        print("--u : used to Display the Usage")    

# Starter
if __name__ == "__main__":
    main()                  # Function Call
