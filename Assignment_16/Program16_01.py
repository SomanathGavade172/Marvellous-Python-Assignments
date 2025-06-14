'''
    1. Write a Python program to create a text file named student.txt and write the names of 5 students into it.

'''

def create_file(filename):
    fobj = open(filename, 'w')
    
    print("Enter name of the 5 students: ")
    for i in range(5):
        name = input()
        fobj.write(name+'\n')

    fobj.close()

    print(f"Student names added to the {filename} successfully.")

def main():
    create_file("student.txt")

if __name__ == "__main__":
    main()