'''
    Q4. Find Largest Among Three Numbers Accept three numbers from the user and print the largest using nested if-else statements.

    Expected Input  :
        Enter three numbers : 5 9 3
    Expected Output :
        Largest number is 9.
'''

# Function Defination
def ChkMax(Value):
    # Logic to check Largest Number
    if(Value[0] >= Value[1]):       # Nested if-else
        if(Value[0] >= Value[2]):       
            print("Largest Number is : ", Value[0])
        else:
            print("Largest Number is : ", Value[2])
    else:
        if(Value[1] >= Value[2]):
            print("Largest Number is : ", Value[1])
        else:
            print("Largest Number is : ", Value[2])
      
# Main Function
def main():
    List = []       # Empty List

    # Logic Input Three Number from User
    print("Enter Three Numbers : ")
    for i in range(3):
        No = int(input())
        List.append(No)

    ChkMax(List)        # Function Call

# Starter
if __name__ == "__main__":
    main()