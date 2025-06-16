'''
    2. Write a program to read and display the contents of a file Data.txt.

'''
# Import os
import os

# Function Defination
def DisplayData(FileName):

    # Check File is Precent Or Not in the Current Directory
    bRet = os.path.exists(FileName)

    if(bRet == True):

        # Open the File in Read Mode
        fobj = open(FileName, "r")

        # Read the Data into the File
        Data = fobj.read()

        # Dispaly Result
        print("Data Read from the File is : \n", Data)

        # File Close
        fobj.close()

    else:
        print("File is Not Precent in the Current Directory")

# Main Function
def main():
    DisplayData("Data.txt") # Function Call

# Starter
if __name__ == "__main__":
    main()                  # Function Call
