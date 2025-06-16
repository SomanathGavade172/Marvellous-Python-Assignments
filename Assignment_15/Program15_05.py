'''
    5. Accept file name and one string from user and return the frequency of that string from file.

    Input : Demo.txt Marvellous
    Search “Marvellous” in Demo.txt

    Output:
            Frequency of String is :  3

'''
# Import Module sys and os
import sys
import os

# Main Function
def main():

    # check Number of Arguments in command line 
    if(len(sys.argv) != 3):
        print("Invalid Input..!")
        return
    
    # Check File is Precent or Not
    bRet = os.path.exists(sys.argv[1])

    if(bRet == True):
        # Open the File
        fobj = open(sys.argv[1], "r")

        # Read the data into the File
        Data = fobj.read()

        # Count the Number of String into the file
        iCount = Data.count(sys.argv[2])

        # Display Result
        print("Frequency of String is : ", iCount)

        # File Close
        fobj.close()

    else:
        print("Given",sys.argv[1], "is not precent in the Current Directory")

# Starter       
if __name__ == "__main__":
    main()                  # Function Call
