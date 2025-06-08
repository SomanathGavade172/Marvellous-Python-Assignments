'''
    3. Create a class Book with private attribute __price. Add methods to get and set the price. Show encapsulation.

'''

# Class Created
class Book:

    # Constructor
    def __init__(self):
        self.__price = 0 
    
    # Instance Method to set Price
    def set(self, price):   
        self.__price = price

    # Instance Method to get Price
    def get(self):          
        return self.__price

# Main Function
def main():
    print("Enter Price of Book : ")
    
    # Accept Integer values only
    try:
        # Accept Book Price from User
        iPrice = int(input())
    except ValueError:
        print("Invalid Input..! Enter Integer Values only..!")
        return

    # Object Created
    bobj = Book()

    # Instance Method Call
    bobj.set(iPrice)

    # Instance Method Call
    iRet = bobj.get()
    print("Book Price is : ", iRet)

# Starter
if __name__ == "__main__":
    main()                  # Function CAll
