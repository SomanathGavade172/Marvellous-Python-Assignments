'''
    8. Write a program which accept one number and display below pattern.

    Input  : 5

    Output :    
                1
                1 2
                1 2 3
                1 2 3 4
                1 2 3 4 5

'''
# Function Defination
def Display(Value):
    # Logic to Display Number Pattern
    for i in range(1, Value + 1):       # Outer Loop
        for j in range(1, i + 1):           # Inner Loop
            print(j, end = " ")
        print()

# Main Function
def main():
    print("Enter a Number : ")
    No = int(input())

    Display(No)     # Function Call

# Starter
if __name__ == "__main__":
    main()