'''
    2. Write a program which contains one class named as BankAccount. BankAccount class contains two instance variables as Name & Amount.
    That class contains one class variable as ROI which is initialise to 10.5. Inside init method initialise all name and amount variables by accepting the values from user.
    There are Four instance methods inside class as Display(), Deposit(), Withdraw(), CalculateIntrest(). Deposit() method will accept the amount from user and add that value in class instance variable
    Amount. Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount. CalculateIntrest() method calculate the interest based on Amount by considering rate of interest
    which is Class variable as ROI. And Display() method will display value of all the instance variables as Name and Amount. After designing the above class call all instance methods by creating multiple objects.

    output:

            Enter Your Name :
            som
            Enter Your Amount :
            5000

            Choose which operation to perform:
            1) Deposit Amount
            2) Withdraw Amount
            3) Exit
            Enter Number of Operation (1, 2, 3):
            1
            Enter amount to deposit:
            500
            500.0 is Successfully Credited..!
            Interest of Current Balance is : 577.5

            ---------------- Account Details ----------------
            Account Holder Name : som
            Account Balance     : 5500.0
            -------------------X--X--X--X--X--X--X-----------
  
'''

# Created Class
class BankAccount:

    # Class Variable (Rate of Interest)
    ROI = 10.5

    # Constructor
    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount
    
    # Deposit Method
    def Deposit(self, dAmount):
        if (dAmount > 0):
            self.Amount = self.Amount + dAmount

            print(dAmount, "is Successfully Credited..!")
        else:
            print("Invalid Deposit Amount..!!")
    
    # Withdraw Method
    def Withdraw(self, wAmount):
        if (wAmount <= self.Amount):
            self.Amount = self.Amount - wAmount

            print(wAmount, "is Successfully Withdrawn..!")
        else:
            print("Insufficient Balance..!! ")
    
    # Calculate Interest Method
    def CalculateIntrest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100

        print("Interest of Current Balance is :", Interest)
    
    # Display Method
    def Display(self):
        print("\n---------------- Account Details ----------------")
        print("Account Holder Name :", self.Name)
        print("Account Balance     :", self.Amount)
        print("-------------------X--X--X--X--X--X--X-------------\n")

# Main Function
def main():

    print("Enter Your Name : ")
    sName = input()

    print("Enter Your Amount : ")
    iAmount = float(input())

    if(iAmount < 0):
        print("Invalid Input..!")
        return

    # Create Object
    obj1 = BankAccount(sName, iAmount)

    while True:
        print("\nChoose which operation to perform:")
        print("1) Deposit Amount")
        print("2) Withdraw Amount")
        print("3) Exit")

        print("Enter Number of Operation (1, 2, 3): ")
        iNo = int(input())

        if iNo == 1:
            print("Enter amount to deposit: ")
            Deposite = float(input())
            obj1.Deposit(Deposite)

        elif iNo == 2:
            print("Enter amount to withdraw: ")
            Withdraw = float(input())
            obj1.Withdraw(Withdraw)

        elif iNo == 3:
            print("Thank You..!")
            return

        else:
            print("Invalid Input..!")
            return

        obj1.CalculateIntrest()
        obj1.Display()

# Starter
if __name__ == "__main__":
    main()  # Function Call
