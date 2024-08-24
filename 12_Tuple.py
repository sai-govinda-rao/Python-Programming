"""
Tuple:
Tuples are used to store multiple items in a single variable.
Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary,
all with different qualities and usage.
A tuple is a collection which is ordered and unchangeable.

Tuple items are ordered, unchangeable, and allow duplicate values.
Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
Syntax:
tuple = (1,2,3,4)
Tuple Methods:
"""
tuple = (10, 20, 30, 40, 50, 20, 20, 20)

#1. count(): This method returns the number of occurrences of an element appearing in a tuple.
print(tuple.count(20))
# output : 4

# index(): This method returns the index position of the specified element
# at the first occurrence in the tuple.
print(tuple.index(20))
# output : 1(element 10 is in the 1st index)

# len(): This built-in method returns the number of elements present in the tuple.
print(len(tuple))
# output : 8

#  max(): This built-in method returns the largest element of a tuple sequence.
print(max(tuple))
# output : 50

# min(): This built-in function returns the smallest element of a tuple.
print(min(tuple))
# output : 10

# sorted(): This method returns a tuple with elements in a sorted order.
print(sorted(tuple))
# output : [10, 20, 20, 20, 20, 30, 40, 50]

# sum(): This method returns the total of all element values of a tuple.
print(sum(tuple))
# output : 210


# some tuple examples
tuple1 = (10,20,30,40,50,20,20,20)
tuple2 = (30,40,50)
tuple = tuple1 + tuple2
print(tuple)
tuple3 = (10,)*10
print(tuple3)
print(tuple1.count(20))
print(len(tuple1))