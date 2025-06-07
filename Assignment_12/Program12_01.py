'''
    1. Write a program which contains one class named as Demo. Demo class contains two instance variables as no1 ,no2. That class contains one class variable as Value.
    There are two instance methods of class as Fun and Gun which displays values of instance variables. Initialise instance variable in init method by accepting the values from user.
    After creating the class create the two objects of Demo class as

    Obj1 = Demo(11,21)
    Obj2 = Demo(51,101)

    Now call the instance methods as

    Obj1.Fun()
    Obj2.Fun()
    Obj1.Gun()
    Obj2.Gun()

'''
# Create a Class
class Demo:
    # Class Variable
    iValue = 0

    # Constructor to Accept Values
    def __init__(self, A, B):
        self.iValue1 = A            # instance variable
        self.iValue2 = B            # instance variable

    # Instance method to Accept Values from User.
    def Fun(self):
        print("First Valuaes is : ", self.iValue1)
        print("Seocnd Value is : ", self.iValue2)

    # Instance method
    def Gun(self):
        print("First Value is : ", self.iValue1)
        print("Second Value is : ", self.iValue2)
        
# Main Function
def main():
    print("Enter First Number : ")

    # Accept Integer Numbers only.
    try:
        # Accept Number from User
        iNo1 = int(input())

    except(ValueError):
        print("Invalid Input..! Enter Numeric Values..!")
        return
    
    print("Enter Second Number : ")

    # Accept Integer Numbers only.
    try:
        # Accept Number from User
        iNo2 = int(input())

    except(ValueError):
        print("Invalid Input..! Enter Numeric Values..!")
        return
    
    # Object Created 1 with User Input Values.
    obj1 = Demo(iNo1, iNo2)

    # Object Created 2 with fixed Values.
    obj2 = Demo(51, 101)

    # Instance method call
    obj1.Fun()
    obj2.Fun()

    # Instance method call
    obj1.Gun()
    obj2.Gun()

# Starter
if __name__ == "__main__":
    main()                  # Function Call