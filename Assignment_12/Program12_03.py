'''
3. Write a program which contains one class named as Arithmetic.
Arithmetic class contains three instance variables as Value1 ,Value2.
Inside init method initialise all instance variables to 0.
There are three instance methods inside class as Accept(), Addition(), Subtraction(),
Multiplication(), Division().
Accept method will accept value of Value1 and Value2 from user.
Addition() method will perform addition of Value1 ,Value2 and return result.
Subtraction() method will perform subtraction of Value1 ,Value2 and return result.
Multiplication() method will perform multiplication of Value1 ,Value2 and return result.
Division() method will perform division of Value1 ,Value2 and return result.
After designing the above class call all instance methods by creating multiple objects.

'''

# Created Calss
class Arithmetic:

    # Cunstructor
    def __init__(self):
        self.iValue1 = 0
        self.iValue2 = 0

    # Instance Method to Accept Values
    def Accept(self, A, B):
        self.iValue1 = A
        self.iValue2 = B

    # Instance Method to Calculate Addition
    def Addition(self):
        iResult = 0
        iResult = self.iValue1 + self.iValue2
        return iResult        

    # Instance Method to Calculate Subtraction 
    def Subtraction (self):
        iResult = 0
        iResult = self.iValue1 - self.iValue2
        return iResult

    # Instance Method to Calculate Multiplication
    def Multiplication(self):
        iResult = 0
        iResult = self.iValue1 * self.iValue2
        return iResult
    
    # Instance Method to Calculate Division
    def Division(self):
        iResult = 0
        iResult = self.iValue1 // self.iValue2
        return iResult
    
# Main Function
def main():
    print("Enter First Number : ")

    # Accept only Integer Values
    try:

        # Accept Number from User.
        iNo1 = int(input())
    except(ValueError):
        print("Invalid Input..! Enter  +Ve Numbers..!")
        return
    
    print("Enter Second Number : ")

    # Accept only Integer Values
    try:
        # Accept Number from User.
        iNo2 = int(input())
    except(ValueError):
        print("Invalid Input..! Enter  +Ve Numbers..!")
        return
    
    # Created object
    aobj1 = Arithmetic()

    # Instance Method Call 
    aobj1.Accept(iNo1, iNo2)

    print("-----------Arithmetic Operation For Obj1-----------")

    iRet = aobj1.Addition()
    print("Addition is : ", iRet)

    iRet = aobj1.Subtraction ()
    print("Subtraction  is : ", iRet)

    iRet = aobj1.Multiplication()
    print("Multiplication is : ", iRet)

    iRet = aobj1.Division()
    print("Division is : ", iRet)


    # Created object
    aobj2 = Arithmetic()

    # Instance Method Call 
    aobj2.Accept(11, 51)

    print("-----------Arithmetic Operation For Obj2-----------")

    iRet = aobj2.Addition()
    print("Addition is : ", iRet)

    iRet = aobj2.Subtraction ()
    print("Subtraction  is : ", iRet)

    iRet = aobj2.Multiplication()
    print("Multiplication is : ", iRet)

    iRet = aobj2.Division()
    print("Division is : ", iRet)

# Starter
if __name__ == "__main__":
    main()                  # Function Call