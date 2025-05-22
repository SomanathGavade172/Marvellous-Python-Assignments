'''
    4. Design python application which creates three threads as small, capital, digits. All the
    threads accepts string as parameter. Small thread display number of small characters,
    capital thread display number of capital characters and digits thread display number of
    digits. Display id and name of each thread.

'''
# Import Module threading.
import threading

# Function Defination.
def Small(Value):
    # Display Thread Name
    print("Name of Thread is : ", threading.current_thread().name)
    print("Id of Small is : ", threading.get_ident())               # Displat TID
    CountSmall = 0

    # Logic to Check Small Character.
    for ch in Value:
        if(ch >= 'a' and ch <= 'z'):
            CountSmall += 1

    print("Number of Small Characters is : ", CountSmall)

# Function Defination.
def Capital(Value):
    # Display Thread Name 
    print("Name of Thread is : ", threading.current_thread().name)
    print("ID of Capital is : ", threading.get_ident())             # Displat TID
    CountCapital = 0

    # Logic to Check Capital Character.
    for ch in Value:
        if(ch >= 'A' and ch <= 'Z'):
            CountCapital += 1

    print("Number of Capital Characters is : ", CountCapital)

# Function Defination.
def Digits(Value):
    # Display Thread Name
    print("Name of Thread is : ", threading.current_thread().name)
    print("ID of Digits is : ", threading.get_ident())              # Displat TID
    CountDigits = 0

    # Logic to Check Digits Character.
    for i in Value:
        if(i >= '0' and i <= '9'):
            CountDigits += 1

    print("Number of Digits is : ", CountDigits)

# Main Function
def main():
    # Accept Input String from User.
    print("Enter a string : ")

    String = str(input())

    # Created Thread Small
    T1 = threading.Thread(target = Small, args = (String,), name = "Small Thread")

    # Created Thread Capital
    T2 = threading.Thread(target = Capital, args = (String,), name = "Capital Thread")

    # Created Thread Digits
    T3 = threading.Thread(target = Digits, args = (String,), name = "Digit Thread")

    # Start Small Thread
    T1.start()

    # Start Capital Thread
    T2.start()

    # Start Digit Thread
    T3.start()

    # Wait for Small thread completes execution.
    T1.join()

    # Wait for Capital thread completes execution.
    T2.join()

    # Wait for Digit thread completes execution.
    T3.join()

# Starter
if __name__ == "__main__":
    main()                  # Function Call