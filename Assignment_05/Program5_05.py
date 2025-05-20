'''
    Q5. Even or Odd Number Check Write a program to check whether the entered number is even or odd.

    Expected Input  :
            Enter a number: 17

    Expected Output :
            17 is an odd number.

'''

# Function Defination
def ChkEvenOdd(Value):
    # Logic to Check given Number is Even or Odd  
    if(Value % 2 == 0):
        return True
    else:
        return False

# Main Function
def main():    
    print("Enter a Number : ")
    # Accept Numeric Values only.
    try:
        No = int(input())
        
    except(ValueError):
        print("Please Enter Integer Numbers..!")
        return 

    Ret = ChkEvenOdd(No)        # Function Call

    # Display Result
    if(Ret == True):
        print(No , "is an Even Number.")
    else:
        print(No, "is an Odd Number.")

# Starter
if __name__ == "__main__":
    main()                  # Function Call
