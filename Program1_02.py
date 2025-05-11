'''
    2. Write a program which contains one function named as ChkNum() which accept one parameter as number. If number is even then it should display “Even number” otherwise
    display “Odd number” on console.

    Input  : 11 
    Output : Odd Number

    Input  : 8   
    Output : Even Number

'''

# Function Defination
def ChkNum():
    print("Enter a Number : ")
    No = int(input())

    # Logic to check Even or Odd Number
    if(No % 2 == 0):
        print("Even Number")
    else:
        print("Odd Number")

# Main Function
def main():
    ChkNum()        # Function Call

# Starter
if __name__ == "__main__":
    main()          # Function Call