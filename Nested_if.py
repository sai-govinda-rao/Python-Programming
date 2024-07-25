# If elif:
"""
if condition1:
    # block of code

elif condition2:
    #block of code

elif condition3:
    #block of code

else:
    #block of code

here first it will check condition 1 if it true execute block of code
in case false check next condition.......until last elif condition
if no conditions satisfies finally execute else block
"""
#Example:

age = int(input("Enter your age:"))
if age < 5:
    print("you are a baby")
elif age < 12:
    print("You are a kid")
elif age < 20:
    print("you are a teenager")
elif age < 30:
    print("You are in young age")
else:
    print("you are aged person")
print("completed Nested_if")

"""
    output:
        Enter your age:10
        You are a kid
        completed Nested_if

"""