'''
    3. Write a program which contains one class named as Numbers. Arithmetic class contains one instance variables as Value. Inside init method initialise that instance variables to the value which is accepted from user.
    There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(), Factors(). ChkPrime() method will returns true if number is prime otherwise return false.
    ChkPerfect() method will returns true if number is perfect otherwise return false. Factors() method will display all factors of instance variable.
    SumFactors() method will return addition of all factors. Use this method in any another method as a helper method if required. After designing the above class call all instance methods by creating multiple objects.

'''
# Class Created
class Number:

    # Constructor
    def __init__(self, Value):
        self.iValue = Value

    # Instance Method to Check Number is Prime
    def ChkPrime(self):
        if(self.iValue <= 1):
            return False
        
        for i in range(2, self.iValue):
            if(self.iValue % i == 0):
                return False
        
        return True

    # Instance Method to check number is Perfect
    def ChkPerfect(self):
        
        if(self.SumFactors == self.iValue):
            return True
        else:
            return False

    # Instance Method to Check Factors
    def Factors(self):
        print("Factors are : ")

        for i in range(1, self.iValue):
            if(self.iValue % i == 0):
                print(i , end = " ")

        print()

    # Instance Method to calculate addition of Factors
    def SumFactors(self):
        iSum = 0

        for i in range(1, self.iValue):
            if(self.iValue % i == 0):
                iSum += i

        return iSum
                
# Main Function
def main():
    print("Enter a Number : ")

    try:
        iNo = int(input())

    except(ValueError):
        print("Invalid Input..! Enter Integer Values..")
        return
    
    # Object Created
    nobj1 = Number(iNo)

    # Instance Method Call
    iRet = nobj1.ChkPrime()
    if(iRet == True):
        print(iNo, "is a Prime Number")
    else:
        print(iNo, "is not a Prime Number")

    # Instance Method Call
    nobj1.Factors()

    # Instance Method Call
    iRet = nobj1.ChkPerfect()
    if(iRet == True):
        print(iNo, "is a Perfect Number")
    else:
        print(iNo, "is Not a Perfect Number")

    # Instance Method Call
    iRet = nobj1.SumFactors()

    print("Addition of Factor is : ", iRet)

# Starter
if __name__ == "__main__":
    main()                  # Function Call