'''
    1. Write a Python program to create a text file named student.txt and write the names of 5 students into it.

'''
# Import Module os
import os

# function Defination
def CreateFile(FName):
    # Open the File in Write Mode
    fobj = open(FName, "w")
    
    print("Enter 5 Students Name : ")
    
    # Accept 5 Name of Student from User
    for i in range(5):
        Name = input()

        # Write Student Name Into the File
        fobj.write(Name + "\n")

    # File is Close
    fobj.close()

    print("Students Name Write into the File : ", FName)

# Main functions
def main():
    print("Enter File Name that you want to Create : ")

    # Accept File Name form User
    FileName = input()

    # Check File is Allready Created
    bRet = os.path.exists(FileName)

    if(bRet == False):
        # Function Call
        CreateFile(FileName)
    else:
        print("File is All Ready Created ..! Please Create another File")

# Starter
if __name__ == "__main__":
    main()                  # Function Call
