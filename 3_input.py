
# Taking input from user
# in python "input(prompt)" is used to taking any type of inputs from user
# prompt is optional it indicates user to which type of data program needed
"""
example:
    a = input("Enter any number:")
    user enter data according to the prompt
    it is not necessary
"""
# python considered user entered data as a string
# we convert this data by using type conversion
# Example:
print("This is input exercise")
print("Hii "+"Hello "+input("What is your name:"))
# Ex2:
a = input("Enter value:")
print(type(a))
# It will print <class 'str'>
# Ex3:
b = int(input("Enter Value:"))  # here we convert data from str to int
print(type(b))
# It will print <class 'int'>

