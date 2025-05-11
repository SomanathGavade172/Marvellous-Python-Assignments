'''
    9. Write a program which display first 10 even numbers on screen.

    Output : 2 4 6 8 10 12 14 16 18 20
'''
# Function Defination
def DisplayEven():
    # Logic to Display first 10 Even Numbers.
    for i in range(2,20 + 1,2):
        print(i, end =" ")

# Main Function
def main():
    DisplayEven()       # Function Call

# Starter
if __name__ == "__main__":
    main()              # Function Call