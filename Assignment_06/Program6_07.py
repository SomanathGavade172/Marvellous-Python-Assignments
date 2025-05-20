'''
    Q7. Accept 5 numbers from the user. Find and print the largest number.

    Expected Input:
                    Enter  5 numbers   : 23 89 12 56 45

    Expected Output:
                    Maximum number is  : 89

'''
# Function Defination
def Maximum(Value):
    iMax = Value[0]

    # Logic to check Maximum Number.
    for i in Value:
        if(iMax < i):
            iMax = i
    
    return iMax

# Main Function
def main():
    List = []       # Empty List

    print("Enter Five Numbers : ")

    # Accept only Integer Numbers.
    try:
        # accept Five Numbers from User.
        for i in range(5):
            No = int(input())
            List.append(No)

    except(ValueError):
        print("Invalide Input..! Enter Numeric Values..!")
        return

    Ret = Maximum(List)     # Function Call

    print("Maximum Number is : ", Ret)

# Starter
if __name__ == "__main__":
    main()                  # Function Call
