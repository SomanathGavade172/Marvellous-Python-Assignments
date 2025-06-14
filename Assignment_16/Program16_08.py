'''
    8. Write a script to remove all blank lines from a file. Save the cleaned output to a new file.

'''


import sys
import os

def remove_blank_space_from_file(old_file,new_file):
    if not os.path.exists(old_file):
        print(f"{old_file} file does not exists in current directory.")

    fobj = open(old_file, 'r')
    data = fobj.read()
    fobj.close()

    filtered_data = data.replace(" ","")
    fobj_new = open(new_file, 'w')
    fobj_new.write(filtered_data)    
    fobj_new.close()

    print(f"All blank spaces removed successfully and updated data copied into {new_file}")

def main():
    if (len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == sys.argv[1] == "--H"):
            print("This application is used to remove all blank lines from a file. Save the cleaned output to a new file ")

        elif(sys.argv[1] == "--u" or sys.argv[1] == sys.argv[1] == "--U"):
            print("Use the given script as ")
            print("ScriptName.py FileName NewFileName")

        else:
            print("Invalid number of command line arguments")
            print("Use the given flags as :")
            print("--h: Used to display the help")
            print("--u: Used to display the usage")

    elif(len(sys.argv) == 3):
        remove_blank_space_from_file(sys.argv[1],sys.argv[2])

    else:
            print("Invalid number of command line arguments")
            print("Use the given flags as :")
            print("--h: Used to display the help")
            print("--u: Used to display the usage")

if __name__ == "__main__":
    main()
