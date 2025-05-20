'''
    Q2. Vowel or Consonant Check Accept a single character from the user and check if it is a vowel (a, e, i, o, u). If not, print it's a consonant.

    Expected Input :
        Enter a character : e
    Expected Output:
        'e' is a vowel.

'''

# Function Defination
def ChkVowel(charX):
    # Logic to check Vowels or Consonant
    if(charX == 'a' or charX == 'e' or charX == 'i' or charX == 'o' or charX == 'u'):
        print(charX , "is a Vowel")
    else:
        print(charX ,"is a Consonant")

# Main Function
def main():
    Value = str(input("Enter a Character : "))

    ChkVowel(Value)     # Function Call

# Starter
if __name__ == "__main__":
    main()              # Function Call