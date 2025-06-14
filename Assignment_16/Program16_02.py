'''
    2. Write a program to read and display the contents of a file data.txt.

'''

import os

def display_file_contents(filename):

    if not os.path.exists(filename):
      print(f"{filename} does not exist in the current directory.")
      exit()

    fobj = open(filename, 'r')

    data = fobj.read()

    print(data)

    fobj.close()

    
def main():
    display_file_contents("data.txt")

if __name__ == "__main__":
    main()