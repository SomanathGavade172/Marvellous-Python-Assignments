'''
    Q6. Write a function that accepts a list of integers and returns a list of prime numbers using filter().

    Expected Input  :
            Enter list  : 10 11 12 13 14 15 16 17

    Expected Output :
        Prime numbers   : [11, 13, 17]

'''

# Function Defination
def ChkPrime(Values):
    if(Values <= 1):
        return False
    # Logic to check Prime Numbers.
    for i in range(2, Values):
        if(Values % i == 0):
            return False
    return True

# Main Function
def main():
    List = []       # Empty List
    print("Enter Number of Elements : ")
    try:
        Size = int(input())
        
        # Accept Numbers from User
        print("Enter", Size ,"Numbers : ")

        for i in range(Size):
            No = int(input())
            List.append(No)

    except(ValueError):
        print("Invalide Input..!Enter Numeric Values...!")
        return
    
    # Filter
    FList = list(filter(ChkPrime, List))    # function Call
    print("Prime Numbers : ", FList)

# Starter
if __name__ == "__main__":
    main()                  # Function Call
    
