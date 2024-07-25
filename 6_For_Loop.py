#ForLoop:
"""
We can iterate string, list, tuple, dictionary and certain range
Range:
    suppose we want to print 1 to 50 numbers
    we can print 50 numbers by using for loop
    syntax:
        for i in range(start, stop, step-size):
            print(i)
        here i is a variable we can take any name in this place
        we must pass stop parameter in this for loop
        start and stop is not mandatory
        defaultly for loop starts from 0 and step size takes to 1
        loop will continue till stop-1
        you must follow the 4 space indentation
"""
for i in range(1, 10, 1):
    print(i)
"""
here clearly we can see it will print till 9
output:
    1
    2
    3
    4
    5
    6
    7
    8
    9
"""
# we can iterate string by using for loop
"""
name = "sai govinda rao"
for i in name:
    print(i)
it will print like below
s
a
i
.
.
.etc

similarly we can iterate list, tuple, .....etc
"""

