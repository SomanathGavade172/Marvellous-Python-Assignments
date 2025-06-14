'''
    5. Accept file name and one string from user and return the frequency of that string from file.

    Input : Demo.txt Marvellous
    Search “Marvellous” in Demo.txt

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
        print("File is Precent is Current Directory")

        fobj = open(sys.argv[1], "w")

        fobj.write("Frequency of Input String is : ", iCount)

        fobj.close()

    else:
        print("Given",sys.argv[1], "is not precent in the Current Directory")
        
if __name__ == "__main__":
    main()