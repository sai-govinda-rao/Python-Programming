"""
List: A list is a collection of different kinds of values or items.
Since Python lists are mutable, we can change their elements after forming.
list elements asign inside the square brackets and separated by comma
"""

# we assign a list on the variable called numbers
numbers = [10, 30, 50, 450, 500, 80, 700, 500, 500, 500, 500, 500, 250]
print(numbers)
"""
output:
    [10, 30, 50, 450, 500, 80, 700, 500, 500, 500, 500, 500, 250]
"""
"""
Here are some list functions in Python: 
count(): Returns the number of elements in a list 
index(): Returns the index of an element in a list 
pop(): Removes an element at a specified index 
remove(): Removes an element from a list 
append(): Adds an element to the end of a list 
clear(): Removes all items from a list 
copy(): Returns a shallow copy of a list 
extend(): Adds iterable elements to the end of a list 
reverse(): Reverses a list 
sort(): Sorts the elements of a list 
len(): Finds the size of a list 

"""

print(len(numbers))
numbers.sort()
numbers.insert(2,45)
# insert element at index number 2

numbers.reverse()
numbers.pop()
numbers.pop(2)
# pop element at the spacified index

print(numbers[2:5])
# access list elements by using slicing concept


numbers.extend([20,40,60])
# add all elements at the end of the list

print(numbers.count(500))
# count the spacified elements how many are there in the list

numbers.append([2])

print(numbers)
"""
output:
    [10, 30, 50, 450, 500, 80, 700, 500, 500, 500, 500, 500, 250]
    13
    [500, 500, 500]
    5
    [700, 500, 500, 500, 500, 500, 450, 250, 80, 50, 45, 30, 20, 40, 60, [2]]
"""
