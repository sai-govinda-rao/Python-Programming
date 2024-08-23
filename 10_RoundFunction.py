"""
It is an inbuilt function which is used to round of the number
used for rounding off numbers up to a specified number of digits after the decimal point.
For example, 65.234 can be rounded off to 65.2
Syntax:
    round(number, round digit)
"""
number = 10.189010109
print(round(number))
"""
output:
    10.19
    if we don't give the round digit it will round the number which is 10
"""
"""
round function write the nearst integer
if we see the below examples
print(round(8.9))
it will return 9 
print(round(9.2))
it will return 9

special case tie  breaking
print(round(7.5))
it will give 8
print(round(6.5))
it will give 6
tie breaking case 
if main number is even then round the same number (6.5 to 6)
if main number is odd then round the next number (7.5 to 8)
"""
print(round(687.5))
print(round(7.5))
print(round(6.5))
"""
output:
    688
    8
    6
"""
