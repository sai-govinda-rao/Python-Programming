"""
Python Dictionary
Dictionaries are a useful data structure for storing data in Python
because they are capable of imitating real-world data arrangements
where a certain value exists for a given key.

The data is stored as key-value pairs using a Python dictionary.
    This data structure is mutable
    The components of dictionary were made using keys and values.
    Keys must only have one component.
    Values can be of any type, including integer, list, and tuple.
"""

dict = {
    "name": "sai",
    "age": 20,
    "Id": 123,
    "gender": "male",
    "salary": 0
}
print(type(dict))
# output : <class 'dict'>

print(dict)
# output : {'name': 'sai', 'age': 20, 'Id': 123, 'gender': 'male', 'salary': 0}

# if we want to get the all keys then use keys() method
print(dict.keys())
# output : dict_keys(['name', 'age', 'Id', 'gender', 'salary'])

# if we want to get all values then use values() method
print(dict.values())
# output : dict_values(['sai', 20, 123, 'male', 0])

# we can access values by using keys shown below
print(dict["name"])
# output : sai

# if we want to add new element to dictionary then follow below process
dict["gmail"] = "sai@gmail.com"
print(dict)
# output : {'name': 'sai', 'age': 20, 'Id': 123, 'gender': 'male', 'salary': 0, 'gmail': 'sai@gmail.com'}
# here is our new key and value added dictionary

# if we want to pop any dict item then use the pop method like below and pass the parameter as key
print(dict.pop("gmail"))
# output : "sai@gmail.com"
print(dict)
# after pop operation our dict is like below
# {'name': 'sai', 'age': 20, 'Id': 123, 'gender': 'male', 'salary': 0}

