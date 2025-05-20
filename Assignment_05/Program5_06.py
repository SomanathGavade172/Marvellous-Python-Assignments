'''
    Q6. Celsius to Fahrenheit Converter Accept temperature in Celsius and convert it to Fahrenheit using the formula: 
        F = (C * 9/5) + 32

    Expected Input  :
            Enter temperature in Celsius : 25

    Expected Output :
            Temperature in Fahrenheit    : 77.0°F

'''
# Function Defination
def CelsiusToFahrenheit(Value):
    # Logic to Convert Celsius to Fahrenheit.
    F = (Value * 9 / 5) + 32

    return F

# Main Function
def main():
    print("Enter a Temperature Celsius : ")
    # Accept Numeric / Decimal Values only.
    try:        
        Temp = float(input())
    
    except (ValueError):
        print("Please Enter Numerical Values")
        return

    Ret = CelsiusToFahrenheit(Temp)      # Function Call

    print("Temperature in Fahrenheit : ", Ret ,"°F")

# Starter
if __name__ == "__main__":
    main()                   # Function Call