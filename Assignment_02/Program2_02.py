'''
2. Write a program which accept one number and display below pattern.

    Input  : 5
    Output :    * * * * *
                * * * * *
                * * * * *
                * * * * *
                * * * * *
'''
# Function Defination
def Display(Value):
    # Logic to print *
    for i in range(Value):
        for j in range(Value):
            print("*", end = ' ')
        print()

# Main Function
def main():
    print("Enter a Number : ")
    No = int(input())

    Display(No)     # Function Call

# Starter
if __name__ == "__main__":
    main()