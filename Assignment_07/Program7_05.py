'''
    Q5. Write a function that accepts a string and checks whether it is a palindrome.

    Expected Input      :
        Enter a string  : radar, madam ,level 

civic

    Expected Output     :
        radar is a palindrome.

'''
# Function Defination
def ChkPalindrome(Value):
    NewString = ''      # Empty String

    # Logic to reverse the String
    for i in range(len(Value) -1, -1, -1):
        NewString = NewString + Value[i]
    return NewString

# Main Function
def main():
    # Accept String from User
    print("Enter the string : ")
    Name = str(input()) 
    
    Ret = ChkPalindrome(Name)       # Function Call

    # Display Result
    if(Ret == Name):
        print(Name ,"is palindrome")
    else:
        print(Name, "is not Palindrome")

# starter
if __name__ == "__main__":
    main()                  # Function Call

