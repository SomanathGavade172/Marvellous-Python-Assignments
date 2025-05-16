# Function Defination

def ChkPrime(num):
    # Filter Number is Greater than 1.
    if num <= 1:
        return False
    
    # Logic to Check Number is Prime Or Not.
    for i in range(2, num):
        if(num % i == 0):
            return False
    return True