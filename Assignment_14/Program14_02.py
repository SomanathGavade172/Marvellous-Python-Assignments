'''
    2. Write a class Rectangle with length and width. Add a method to compute area and perimeter.
    
    Area: 50, Perimeter: 30

'''
# Class Created
class Rectangle:

    # constructor
    def __init__(self, Length, Width):
        self.fLength = Length
        self.fWidth = Width

    # Instance Method to Calculate Area
    def CalculateArea(self):
        Area = 0.0
        Area = self.fLength * self.fWidth
        return Area
    
    # Instance Method to Calculate Perimeter
    def CalculatePerimeter(self):
        Perimeter = 0.0
        Perimeter = 2 * (self.fLength + self.fWidth )
        return Perimeter

# Main Function
def main():
    # Accept Length from User
    print("Enter a Length of Rectangle : ")
    fLength = float(input())

    # Accept Width from User
    print("Enter Width of Rectangle : ")
    fWidth = float(input())

    # Object Created
    obj = Rectangle(fLength, fWidth)

    # Instance Method Call
    fRet = obj.CalculateArea()
    print("Area is : ", fRet)

    # Instance Method Call
    fRet = obj.CalculatePerimeter()
    print("Perimeter is : ", fRet)

# starter
if __name__ == "__main__":
    main()                  # Function Call