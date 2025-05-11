'''
    5. Write a program which display 10 to 1 on screen.

    Output : 10 9 8 7 6 5 4 3 2 1
'''
# Function Defination
def Display():
    # Logic to print Numbers from 10 to 1.
    for i in range(10, 0, -1):
        print(i, end = " ")    # end = " " : which is used to print on same line. 

# Main Function
def main():
    Display()       # Function Call

# Starter 
if __name__ == "__main__":
    main()          # Function Call