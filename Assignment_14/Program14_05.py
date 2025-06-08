'''
    5. Create a class BankAccount with account_number, name, and balance. Use __init__ and create methods for deposit, withdraw, and displaying balance.

    Input :
        Enter Account Number : 123456789
        Enter Your Name      :  somanath
        Enter your Balance   : 5000
        Enter which Operation You can Perform(1,2,3,4) : 1)DisplayBankDetails 2)Deposite 3)Withdraw  4)Exit
        Your choice is :  1
        
    Output :
        ----------------Bank Details----------------
        Account Number is :  123456789
        Name of Account Holder is :  somanath
        Total Balance is :  5000
        ---------------X-X-X-X-X-X-X-X---------------
'''
# Class Created
class BankAccount:

    # Constructor
    def __init__(self,account_number, name, balance):
        self.Account_Number = account_number
        self.Name = name
        self.Balance = balance

    # Instance MEthod to Deposite Amount
    def Deposite(self, dAmount):
        # Check Amount is not a -ve
        if(dAmount > 0):
            self.Balance += dAmount
            print(dAmount , "is Creatited Successfully..!!")
        else:
            print("Invalid Input..")

    # Instance MEthod to Withdraw Amount
    def Withdraw(self,wAmount):
        # check withdraw amount is less than balance
        if(wAmount > self.Balance):
            print("Insufficient Balance..!")
        elif(wAmount <= 0):
            print("Invalid Withdraw Amount..!")
        else:
            self.Balance -= wAmount
            print(wAmount, "is successfully Debited..!!")

    # Instance MEthod to Display BAnk Details
    def DisplayBankDetails(self):
        print("\n----------------Bank Details----------------")
        print("Account Number is : ", self.Account_Number)
        print("Name of Account Holder is : ", self.Name)
        print("Total Balance is : ", self.Balance)
        print("---------------X-X-X-X-X-X-X-X---------------\n")

# MAin Function
def main():

    print("Enter Account Number : ")
    try:
        # Accept Account Number from User.
        Ac_No = int(input())
    except(ValueError):
        print("Invalid Input..! Enter Integer Number..!")
        return
    
    print("Enter Your Name : ")
    # Accept Name from User.
    Name = input()

    print("Enter your Balance : ")
    try:
       # Accept Balanace from User.
       Balance = int(input())
    except(ValueError):
        print("Invalid Input..! Enter Integer Number..!")
        return

    # Object Created
    bobj = BankAccount(Ac_No, Name, Balance)
    
    while(True):
        print("Enter which Operation You can Perform(1,2,3,4) : ")
        print("1)DisplayBankDetails \n2)Deposite \n3)Withdraw \n4)Exit")

        try:
            # Accept operation from User.
            iNo = int(input())
            print("Your choice is : ", iNo)
        except(ValueError):
                print("Invalid Input..! Enter Integer Number..!")
                return
        
        # Check the conditions
        if(iNo == 1):
            bobj.DisplayBankDetails()       # Instance Method call

        elif(iNo == 2):
            print("Enter How many Amount You can Deposite : ")
            try:
                DepositeAmount = int(input())
            except(ValueError):
                    print("Invalid Input..! Enter Integer Number..!")
                    return

            bobj.Deposite(DepositeAmount)   # Instance Method call
            bobj.DisplayBankDetails()       # Instance Method call

        elif(iNo == 3):
            print("Enter How many Amount you want to Withdraw : ")
            try:
                WithDrawAmont = int(input())
            except(ValueError):
                    print("Invalid Input..! Enter Integer Number..!")
                    return
            
            bobj.Withdraw(WithDrawAmont)    # Instance Method call
            bobj.DisplayBankDetails()       # Instance Method call

        elif(iNo == 4):
            print("Thank You...! Have a Good Day..!")
            return
        
        else:
            print("Sorry..! Invalid Input..! Please Try again..!")
            return

# Starter
if __name__ == "__main__":
    main()                  # Function call