'''
    6. Write a program which accept number from user and check whether that number is positive or negative or zero.

    Input  : 11 
    Output : Positive Number

    Input  : -8 
    Output : Negative Number

    Input  : 0 
    Output : Zero
'''
# Function Defination
def ChkNum(No):
    # Lofic to check whether the number is Positive or Negative or Zero.
    if (No > 0):
        print("Positive")
    elif (No < 0):
        print("Negative")
    else:
        print("Zero")

def main():
    Value = int(input("Enter a Number : "))

    ChkNum(Value)       # Function Call

# Starter
if __name__ == "__main__":
    main()              # Function Call