'''
    Q1. Write a program using a while loop to print numbers from 1 to 50.

    Expected Output:
                    1 2 3 4 ... 50

'''
# Function Defination
def Display(Value):
    i = 1
    # Logic to Display Number from 1 to 50.
    while(i <= Value):
        print(i , end = " ")
        i = i + 1
    print()

# Main Function
def main():

    Display(50)     # Function Call

# Starter
if __name__ == "__main__":
    main()