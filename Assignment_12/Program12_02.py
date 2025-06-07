'''
    2. Write a program which contains one class named as Circle. Circle class contains three instance variables as Radius ,Area, Circumference. That class contains one class variable as PI which is initialise to 3.14. Inside init method initialise all instance variables to 0.0.
    There are three in stance methods in side classas Accept() , CalculateArea() , CalculateCircumference(), Display(). Accept method will accept value of Radius from user.
    CalculateArea() method will calculate area of circle and store it into instance variable Area. CalculateCircumference() method will calculate circumference of circle and store it into instance
    variable Circumference. And Display() method will display value of all the instance variables as Radius , Area, Circumference. After designing the above class call all instance methods by creating multiple objects.

    Input  : 
            Enter Raduius of Circle    :  5.3

    Output :
            Radius od Circle is        :  5.3
            Area of Circle is          :  88.20259999999999
            Circumference of Circle is :  33.284
'''

# Created Calss
class Circle:
    # Class Variable
    PI = 3.14

    # Constructor
    def __init__(self):
        self.fRadius = 0.0              # Instance Variable
        self.fArea = 0.0                # Instance Variable
        self.fCircumference = 0.0       # Instance Variable

    # Instance Method to accept radius
    def Accept(self, A):    
        self.fRadius = A

    # Instance Method to Calculate Area
    def CalculateArea(self):
        self.fArea = Circle.PI * self.fRadius * self.fRadius

    # Instance Method to Calculate Circumference
    def CalculateCircumference(self):
        self.fCircumference = 2 * Circle.PI * self.fRadius

    # Instance Method to Display radius, area, and circumference
    def Display(self):
        print("Radius od Circle is : ", self.fRadius)
        print("Area of Circle is  : ", self.fArea)
        print("Circumference of Circle is : ", self.fCircumference)

# Main Function
def main():

    print("Enter Raduius of Circle : ")

    # Accept Integer Numbers 
    try:
        # Accept Number of Elements from User
        iNo = float(input())

        # Check Number is -Ve
        if(iNo < 0):
            print("Invalid Input..! Enter +ve Number..!")
            return
        
    except(ValueError):
        print("Invalid Input..! Enter +ve Numbers..!")
        return
    
    # Object Created
    obj1 = Circle()
    obj2 = Circle()

    # Instance Method Call
    obj1.Accept(iNo)

    print("-----------Circle Calculation for obj1-----------")

    obj1.CalculateArea()
    obj1.CalculateCircumference()

    obj1.Display()

    # Instance Method Call
    obj2.Accept(5.5)

    print("-----------Circle Calculation for obj2-----------")
    obj2.CalculateArea()
    obj2.CalculateCircumference()

    obj2.Display()

# Starter
if __name__ == "__main__":
    main()                  # Function Call