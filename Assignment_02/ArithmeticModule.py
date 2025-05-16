'''

1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, Mult() for multiplication and Div() for division.

'''
# Function Defination
def Add(Value1, Value2):
    Ans = Value1 + Value2
    return Ans

# Function Defination
def Sub(Value1, Value2):
    Ans = Value1 - Value2
    return Ans

# Function Defination
def Mult(Value1, Value2):
    Ans = Value1 * Value2
    return Ans

# Function Defination
def Div(Value1, Value2):
    # Filter to check Division by zero is not allowed.
    if(Value2 != 0):
        Ans = Value1 / Value2
    else:
        return "Division by zero is not allowed"
    return Ans