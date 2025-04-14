# https://github.com/dshvetsov2025/lab10-DS-CZ
# Partner 1: Dmitrii Shvetsov
# Partner 2: Case Zumbrum


import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot perform a square root of a negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    if a < 0:
        return math.hypot(a, b)
    if b < 0:
        return math.hypot(a, b)
    else:
        return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid input for logarithm. Base must be > 0 and ≠ 1; value must be > 0.")
    return math.log(b, a)

def exponent(a, b):
    return a ** b


