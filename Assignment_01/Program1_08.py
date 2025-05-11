'''
    8. Write a program which accept number from user and print that number of “*” on screen.

    Input  : 5 
    Output : * * * * *
'''
# Function Defination
def Display(No):
    # Logic to Display *
    for i in range(No):
        print("*", end = " ")

# Main Function
def main():
    Value = int(input("Enter a Number : "))

    Display(Value)          # Function Call

# Starter
if __name__ == "__main__":
    main()                  # Function Call