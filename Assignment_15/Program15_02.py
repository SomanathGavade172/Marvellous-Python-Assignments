'''
    2. Write a program which accept file name from user and open that file and display the contents of that file on screen.

    Input :
            Enter the File Name that you want to Open :  Demo.txt
    
            Data read as :  Welcome To Marvellous Family.

'''
# Import Module os
import os

# Main Function
def main():

    print("Enter the File Name that you want to Open : ")
    
    # Accept File Name form User.
    FileName = input()

    # Check File is present or not.
    bRet = os.path.exists(FileName)

    if(bRet == True):
        # File is open
        fobj = open("Demo.txt", "r")

        # Data save after reading the file into to data
        data = fobj.read()

        # Display Read data
        print("Data read as : ", data)

        # File is close
        fobj.close()
    else:
        print("File is Not Precent in Current F+Directory..!")

# starter
if __name__ == "__main__":
    main()                  # Function Call