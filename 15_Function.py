"""
A function is a set of statements that take inputs, do some specific computation, and produce output.
The idea is to put some commonly or repeatedly done tasks together
and make a function so that instead of writing the same code again and again for different inputs,
we can call the function. Functions that readily come with Python are called built-in functions.
Python provides built-in functions like print(), etc.
but we can also create your own functions. These functions are known as user defines functions.


* Once defined, Python functions can be called multiple times and from any location in a program.
* Our Python program can be broken up into numerous, easy-to-follow functions if it is significant.
* The ability to return as many outputs as we want using a variety of arguments is one of Python's
  most significant achievements.
* However, Python programs have always incurred overhead when calling functions.
* However, calling functions has always been overhead in a Python program.

Syntax

#  An example Python Function
def function_name( parameters ):
    # code block
"""
# Example 1
def great():
    print("Hi")
    print("Hello")
great()

# output : Hi
        # Hello
# Example 2
def Addition(a, b):
    sum = a+b
    return sum
print(Addition(10, 20))

# output : 30
# A return expression can get a value from a defined function.
# once we create the function we can use it many times according to our need
# functions are used to reduce the code and increase the code re-usability
