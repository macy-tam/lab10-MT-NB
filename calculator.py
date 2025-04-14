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
    if a == 0:
        raise ValueError

    return math.sqrt(a)

def hypotenuse(a, b):
    math.hypot(a, b)

def subtract(a, b):
    a - b

def logarithm(a, b):
    if b<=0:
        raise ValueError
    math.log(b,a)

def add(a, b): a + b

def mul(a, b): a * b

def div(a, b): # raise ZeroDivisionError if a == 0
    if a == 0:
        raise ZeroDivisionError
    else: b / a

def exp(a, b): a**b
