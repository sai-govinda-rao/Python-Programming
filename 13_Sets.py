"""
Set:
A Python set is the collection of the unordered items.
set support mixed elements it means a single set contain multiple data types
Each element in the set must be unique, immutable, and the sets remove the duplicate elements.
Sets are mutable which means we can modify it after its creation.
The set can be created by enclosing the comma-separated immutable items with the curly braces {}
Syntax:
    set1 = {1, 20, "Sai", False, 10.10}
"""
set1 = {10,20,10,True,"Sai",30,50,80}
print(type(set1))
# output : <class 'set'>

# add() : The add() method adds a given element to a set.
# If the element is already present, it doesn't add any element.
new_element = 600
set1.add(new_element)
print(set1)
# output : our set after adding new element
# {80, True, 50, 'sai', 20, 600, 10, 30}
# out set before adding new element
# {80, True, 50, 20, 'sai', 10, 30}

# clear() : The clear() method removes all items from the set.
#set1.clear()
print(set1)
# output : set()
# it will print the empty set like above

# remove() : The remove() method removes the specified element from the set.
set1.remove(10)
print(set1)
# output : {'sai', True, 80, 50, 20, 600, 30}

# len() : we can find the length of the set by using length function
print(len(set1))
# output : 7

# The pop() method randomly removes an item from a set and returns the removed item.
pop_element = set1.pop()
print('pop element is:', pop_element)
# output : 'sai'

# difference() : The difference() method computes the difference of two sets
#and returns items that are unique to the first set. difference means set1-set2
set2 = {10, True, 1, "Sai", "No", 20, 30}
print(set1.difference(set2))
print(set2.difference(set1))
# output : {600, 50}
#         {'No', 10}


# The symmetric_difference() method returns all the items present in given sets,
# except the items in their intersections.
print(set1.symmetric_difference(set2))
# set1 = {True, 50, 20, 600, 'Sai', 30}
# set2 = {True, 'No', 20, 10, 'Sai', 30}
# output : {50, 'No', 10, 600}