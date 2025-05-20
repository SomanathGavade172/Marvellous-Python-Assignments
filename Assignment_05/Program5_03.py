'''
    Q3. Voting Eligibility Checker Accept age from the user and check whether the person is eligible to vote. (Age should be 18 or above.)

    Expected Input:
                        Enter age: 19
    Expected Output:
                        Eligible to vote.

'''

# Function Defination
def ChkEligible(No):
    # Logic to Check person is eligible to vote
    if(No >= 18):
        return True
    else:
        return False

# Main Function
def main():
    Age = int(input("Enter your Age : "))

    Result = ChkEligible(Age)       # Function Call

    # Display Result
    if(Result == True):
        print("Eligible to Vote.")
    else:
        print("Not Eligible to Vote.")

# Starter
if __name__ == "__main__":
    main()