# importing libraries 
from sortedcontainers import SortedList, SortedSet, SortedDict

# initializing a sorted set with parameters
# it takes an iterable as an argument
sorted_set = SortedSet([1, 1, 2, 3, 4])

# initializing a sorted set using default constructor
sorted_set = SortedSet()

# inserting values one by one
for i in range(5, 0, -1):
    sorted_set.add(i)

print('set after adding elements: ', sorted_set)

# inserting duplicate value
sorted_set.add(5)

print('set after inserting duplicate element: ', sorted_set)

# discarding an element
sorted_set.discard(4)

print('set after discarding: ', sorted_set)

# checking membership using 'in' operator
if(2 in sorted_set):
    print('2 is present')
else:
    print('2 is not present')

print('set elements are: ', end = '')

# iterating through a sorted set
for i in sorted_set:
    print(i, end = ' ')
print()