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
def add(a, b): 
    a+b

def subtract(a, b):
    a - b

def multiply(a, b):
    a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    b / a

def logarithm(a, b):
    if b<=0:
        raise ValueError
    math.log(b,a)

def exponent(a, b):
    a**b

import math
def add(a, b): a + b

def sub(a, b): a - b

def mul(a, b): a * b

def div(a, b): # raise ZeroDivisionError if a == 0
    if a == 0:
        raise ZeroDivisionError
    else: b / a

def log(a, b): # use math library + raise ValueError
    #did not say raise value error if
    math.log(b, a)
    raise ValueError

def exp(a, b): a**b
