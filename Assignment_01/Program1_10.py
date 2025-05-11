'''
    10. Write a program which accept name from user and display length of its name.

    Input  : Marvellous 
    Output : 10
'''
# Function Defination
def DisplayLength(Name):
    # Logic to count length
    count = 0
    for i in Name:
        count += 1
    return count

    # Logic to count length using built-in len() function 
    # count = len(Name)
    # return count

# Main Function
def main():
    Value = input("Enter your Name : ")

    Result = DisplayLength(Value)       # Function Call

    print("Length is : ", Result)

# Main Function
if __name__ == "__main__":
    main()                              # Function Call