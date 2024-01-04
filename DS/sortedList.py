# importing libraries 
from sortedcontainers import SortedList, SortedSet, SortedDict

# initializing a sorted list with parameters
# it takes an iterable as a parameter.
sorted_list = SortedList([1, 2, 3, 4])

# initializing a sorted list using default constructor
sorted_list = SortedList()

# inserting values one by one using add()
for i in range(5, 0, -1):
    sorted_list.add(i)

print('len = ', len(sorted_list))
# prints the elements in sorted order
print('list after adding 5 elements: ', sorted_list)

print('list elements are: ', end = '')

# iterating through a sorted list
for i in sorted_list:
    print(i, end = ' ')
print()

# removing all elements using clear()
sorted_list.clear()

# adding elements using the update() function
elements = [10, 9, 8, 7, 6]

sorted_list.update(elements)

# prints the updated list in sorted order
print('list after updating: ', sorted_list)

# removing a particular element
sorted_list.discard(8)

print('list after removing one element: ', sorted_list)

# removing all elements
sorted_list.clear()

print('list after removing all elements using clear: ', sorted_list)
