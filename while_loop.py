#While Loop
"""
While loop is also known as a pre-tested loop. In general,
a while loop allows a part of the code to be executed multiple times
depending upon a given boolean condition.
* first Check the Condition
* if Condition True Execute Block of code
* after Increment
Syntax:
while Condition:
    //Block of Code

    value Increment
while loop also has else block. it works same as for else
If while Successfully Completed Then execute else block
if loop will be break by any chance then else block doesn't Execute
"""


#Example 1
num = int(input("Enter the number:"))  # number taken by user
count = 0
while count <= num:  # Condition
    print(count)
    count += 1  # increment
    # loop run untill count is equals to user entered number

"""
output:
    Enter the number:5
    0
    1
    2
    3
    4
    5
"""



# while Else Example
# else block execute Example2
count = 0
number = 5
while count <= number:  # Condition
    print("Hello", count)
    count += 1  # Increment
else:
    print("Loop Successfully Completed")
"""
output:
    Hello 0
    Hello 1
    Hello 2
    Hello 3
    Hello 4
    Hello 5
    Loop Successfully Completed
"""



# else block not executed Example3
count = 0
number = 10
while count <= number:  # Condition
    print("Hello", count)
    count += 1  # Increment
    if count == 5:  # Again Loop break Condition
        break
else:
    print("Loop Successfully Completed")

"""
output:
    Hello 0
    Hello 1
    Hello 2
    Hello 3
    Hello 4
"""



