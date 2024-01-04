# importing libraries
from sortedcontainers import SortedList, SortedSet, SortedDict

# initializing a sorted dict with parameters
# it takes a dictionary object as a parameter
# sorted_dict = SortedDict({'a': 1, 'b': 2, 'c': 3})

# initializing a sorted dict
sorted_dict = SortedDict({'a': 1, 'c': 2, 'b':3})

# print the dict
print('sorted dict is: ', sorted_dict)

# adding key => value pairs
sorted_dict['d'] = 3

print('sorted dict after adding an element: ', sorted_dict)

# adding element using setdefault()
sorted_dict.setdefault('e', 4)

print('sorted dict after setdefault(): ', sorted_dict)

# using the get function
print('using the get function to print the value of a: ', sorted_dict.get('a', 0))

# checking membership using 'in' operator
if('a' in sorted_dict):
    print('a is present')
else:
    print('a is not present')

print('dict elements are: ', end = '')

# iterating over key => value pairs in a dictionary
for key in sorted_dict:
    print('{} -> {}'.format(key, sorted_dict[key]), end = ' ')
print()

# removing all elements from the dict
sorted_dict.clear()

print('sorted dict after removing all elements: ', sorted_dict)