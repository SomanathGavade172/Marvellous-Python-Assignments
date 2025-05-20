'''
    Q7. Area and Perimeter of Rectangle Accept the length and width of a rectangle. Calculate and display the area and perimeter.

    Expected Input:
            Enter length :  5
            Enter width  :  3

    Expected Output:
            Area         :  15
            Perimeter    :  16

'''
# Function Defination
def Area(Value1, Value2):
    # Logic to Calculate Area of Rectangle
    Ans = Value1 * Value2
    return Ans

# Function Defination
def Perimeter(Value1, Value2):
    # Logic to Calculate Perimeter of Rectangle
    Ans = 2 * (Value1 + Value2)
    return Ans

# Main Function
def main():
    # Accept Numeric Values only.
    try:
        print("Enter a Length : ")
        Length = int(input())

        print("Enter the Width : ")
        Width = int(input())

    except (ValueError):
        print("Please Enter Numeric Values..!")
        return 

    Ret = Area(Length, Width)               # Function Call
    print("Area of Rectangle is : ", Ret)

    Ret = Perimeter(Length, Width)          # Function Call
    print("Perimeter of Rectangle is : ", Ret)

# Starter
if __name__ == "__main__":
    main()                  # Function Call