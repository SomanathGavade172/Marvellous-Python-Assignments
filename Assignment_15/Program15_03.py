'''
    3. Write a program which accept file name from user and create new file named as Demo.txt and copy all contents from existing file into new file. Accept file name through command line
    arguments.

    Input : python Program15_03.py ABC.txt Demo.txt (ABC.txt)
            Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt

    Output:
            Number of command line arguments :  3
            ABC.txt File is present in Current Directory
            Copied Data in New File(Demo.txt) is :  Welcome To Marvellous Family.
'''
# Import Module sys and os
import sys
import os

# main function
def main():
    # Display Number of Command Line Arguments
    print("Number of command line arguments : ", len(sys.argv))

    # # Check if exactly 2 arguments provide
    if(len(sys.argv) != 3):
        print("Invalid Input..! Use python fileName.py (MainFile.txt) (CopiedFile.txt) ")
        return

    # Check File is Precent in current Directory
    bRet = os.path.exists(sys.argv[1])  

    # 
    if(bRet == True):
        print(sys.argv[1],"File is present in Current Directory")

        # Main File is Open in Read Mode
        fobj = open(sys.argv[1], "r") 
        Data = fobj.read()              # Read the Data
        fobj.close()                    # File is Close

        # Copied File is Open in Write Mode
        Newfobj = open(sys.argv[2], "w") 
        Newfobj.write(Data)                # Data Write into Copied File
        Newfobj.close()                     # File is Close

        # Open Copied FIle in Read Mode
        Newfobj = open(sys.argv[2], "r")
        CopyData = Newfobj.read()           # Read the Data
        Newfobj.close()                     # File is Close

        # Display the Copied Data
        print("Copied Data in New File(",sys.argv[2],")is : ", CopyData)        

    else:
        print("Given ",sys.argv[1],"File does not exist in the current directory.")

# Starter
if __name__ == "__main__":
    main()                  # Function Call
