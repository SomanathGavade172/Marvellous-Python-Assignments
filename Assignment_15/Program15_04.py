'''
    4. Write a program which accept two file names from user and compare contents of both the
    files. If both the files contains same contents then display success otherwise display failure.
    Accept names of both the files from command line.

    Input : Demo.txt Hello.txt
    Compare contents of Demo.txt and Hello.txt

'''
import sys
import os

def main():
    print("Number of Command Line Arguments is : ", len(sys.argv))

    if(len(sys.argv) != 3):
        print("Invalid Input..!")
        return
    
    bRet = os.path.exists(sys.argv[1])

    if(bRet == True):
        print("Files are Precent in the Current Directory")

        fobj = open(sys.argv[1], "r")
        Data1 = fobj.read()
        fobj.close()

        fobj2 = open(sys.argv[2], "r")
        Data2 = fobj2.read()
        fobj2.close()

        if(Data1 == Data2):
            print("Success")
        else:
            print("Failure")

if __name__ == "__main__":
    main()