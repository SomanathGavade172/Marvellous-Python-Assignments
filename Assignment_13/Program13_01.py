'''
    1. Write a program which contains one class named as BookStore. BookStore class contains two instance variables as Name ,Author. That class contains one class variable as NoOfBooks which is initialise to 0.
    There is one instance methods of class as Display which displays name , Author and number of books. Initialise instance variable in init method by accepting the values from user as name and author.
    Inside init method increment value of NoOfBooks by one. After creating the class create the two objects of BookStore class as Obj1 = BookStore(“Linux System Programming”, “Robert Love”)
    Obj1.Display() # Linux System Programming by Robert Love. No of books : 1 Obj2 = BookStore(“C Programming”, “Dennis Ritchie”) Obj2.Display() # C Programming by Dennis Ritchie. No of books : 2

    Output:
            -------------Book Details----------------
            Linux System Programming by Robert Love No of Book :  1

            -------------Book Details----------------
            C Programming by Dennis Ritchie No of Book :  2
'''
# Class Created
class Bookstore:
    
    # Class Variable
    iNoOfBooks = 0

    # Constructor
    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author

        Bookstore.iNoOfBooks += 1

    # Instance Method to Display Book details
    def Display(self):
        print(self.Name ,"by", self.Author,"No of Book : " ,self.iNoOfBooks)

# Main Function
def main():

    # Object Created
    obj1 = Bookstore("Linux System Programming", "Robert Love")
    
    # Instance Method call
    print("-------------Book Details----------------")
    obj1.Display()

    # Objected Created 
    obj2 = Bookstore("C Programming", "Dennis Ritchie")
    
    # Instance Method Call
    print("-------------Book Details----------------")
    obj2.Display()

# Starter
if __name__ == "__main__":
    main()                  # Function Call