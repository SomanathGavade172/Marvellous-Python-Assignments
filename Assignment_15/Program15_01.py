'''
    1.Write a program which accepts file name from user and check whether that file exists in current directory or not.

    Input : Demo.txt
    Check whether Demo.txt exists or not.

'''
# Import Module os
import os

# Main Function
def main():
    # Accept File Name from User.
    print("Enter the name of File that you want to Search : ")

    FileName = input()

    # Logic to check File is precent or not.
    bRet = os.path.exists(FileName)

    # Display Result
    if(bRet == True):
        print("File is Precent in the Current Directory")
    else:
        print("There is a No such File..!!")

# Starter
if __name__ == "__main__":
    main()                  # Function Call