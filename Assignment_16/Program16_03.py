'''
    3. Write a Python script to count the number of lines, words, and characters in a given file.

'''

import os
import sys

def file_content_info(filename):
    if not os.path.exists(filename):
        print(f"{filename} does not exist in the current directory.")
        exit()
    
    fobj = open(filename,'r')
    data = fobj.read()

    number_of_characters = len(data)

    print('Number of characters in text file: ', number_of_characters)

    words = data.split()

    print('Number of words in text file : ', len(words))

    with open(filename, 'r') as fp:
        for count, line in enumerate(fp):
            pass
    
    print('Number of lines in text file : ', count+1) #As counting start from 0
    # print(x)
    fobj.close()

def main():
    if (len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == sys.argv[1] == "--H"):
            print("This application is used to count the number of lines, words, and characters in a given file")

        elif(sys.argv[1] == "--u" or sys.argv[1] == sys.argv[1] == "--U"):
            print("Use the given script as ")
            print("ScriptName.py FileName")

        else:
            file_content_info(sys.argv[1])

    else:
      print("Invalid number of command line arguments")
      print("Use the given flags as :")
      print("--h: Used to display the help")
      print("--u: Used to display the usage")

if __name__ == "__main__":
    main()