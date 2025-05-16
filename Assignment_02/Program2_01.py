'''
1. Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
parameters as number and perform the operation. Write on python program which call all the functions from Arithmetic module by accepting the parameters from user.

'''
# import module Arithmatic
import ArithmeticModule

# Main Function
def main():
    while(True):
        print("\n")
        print("1. Add")
        print("2. Sub")
        print("3. Mul")
        print("4. Div")
        print("5. Exit")

        print("Select which mathematical operation you can perform : ")
        operation  = input()

        if(operation == 'Exit'):
            break

        if operation not in ['Add', 'Sub', 'Mul', 'Exit']:
            print("Invalid input. . . ! Please enter Valide Operater")
            continue  

        No1 = int(input("Enter First Number : "))
        No2 = int(input("Enter Second Number : "))

        if(operation == 'Add'):
            Result = ArithmeticModule.Add(No1, No2)       # Function Call
            print("Addition is : ", Result)

        elif(operation  == 'Sub'):
            Result = ArithmeticModule.Sub(No1, No2)       # Function Call
            print("Substraction is : ", Result)
        
        elif(operation  == 'Mul'):
            Result = ArithmeticModule.Mult(No1, No2)      # Function Call
            print("Multiplication is : ", Result)

        elif(operation  == 'Div'):
            Result = ArithmeticModule.Div(No1, No2)       # Function Call
            print("Division is : ", Result)

        else:
            print("Invalid Input. . . ! Plese try again")

# Starter
if __name__ == "__main__":
    main()