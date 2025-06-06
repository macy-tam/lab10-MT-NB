#https://github.com/macy-tam/lab10-MT-NB.git
#Partner 1: Macy Tam
#Partner 2: Nicholas Batchelor
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def square_root(a):
    if a < 0:
        raise ValueError

    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def subtract(a, b):
    return a - b

def logarithm(a, b):
    if b<=0:
        raise ValueError
    return math.log(b,a)

def add(a, b): return a + b

def mul(a, b): return a * b

def div(a, b): # raise ZeroDivisionError if a == 0
    if a == 0:
        raise ZeroDivisionError
    else: return b / a

def exp(a, b): return a**b
