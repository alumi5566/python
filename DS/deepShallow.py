import copy

print("===Use '=' on list ===")
old_list = [1, 2, 3]
new_list = old_list
print('Old List ID:', id(old_list), ". Old List: ", old_list)
print('New List ID:', id(new_list), ". New List: ", new_list)
new_list[2] = 9
print("Update new_list[2][2] = 9")
print('Old List ID:', id(old_list), ". Old List: ", old_list)
print('New List ID:', id(new_list), ". New List: ", new_list)
old_list.append(4)
print("Update old_list.append([4, 4, 4])")
print('Old List ID:', id(old_list), ". Old List: ", old_list)
print('New List ID:', id(new_list), ". New List: ", new_list)

print("===Use copy.copy ===")
old_list = [[1,2], [3,4]]
new_list = copy.copy(old_list)
print('Old List ID:', id(old_list), ". Old List: ", old_list)
print('New List ID:', id(new_list), ". New List: ", new_list)
old_list[1][1] = 100
print("Update old_list[1][1] = 100 ")
print('Old List ID:', id(old_list), ". Old List: ", old_list)
print('New List ID:', id(new_list), ". New List: ", new_list)
old_list.append([5, 6])
print("Update old_list.append([5, 6]) ")
print('Old List ID:', id(old_list), ". Old List: ", old_list)
print('New List ID:', id(new_list), ". New List: ", new_list)


print("===Use '=' on list ===")
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list
print('Old List ID:', id(old_list), ". Old List: ", old_list)
print('New List ID:', id(new_list), ". New List: ", new_list)
new_list[2][2] = 9
print("Update new_list[2][2] = 9")
print('Old List ID:', id(old_list), ". Old List: ", old_list)
print('New List ID:', id(new_list), ". New List: ", new_list)
old_list.append([4, 4, 4])
print("Update old_list.append([4, 4, 4])")
print('Old List ID:', id(old_list), ". Old List: ", old_list)
print('New List ID:', id(new_list), ". New List: ", new_list)

print("===Use '=' on var ===")
a = 10
b = a
print("a ID:", id(a), ". a:", a)
print("b ID:", id(b), ". b:", b)
a += 1
print("Update a += 1")
print("a ID:", id(a), ". a:", a)
print("b ID:", id(b), ". b:", b)

print("===Use '=' on string ===")
a = "aaa"
b = a
print("a ID:", id(a), ". a:", a)
print("b ID:", id(b), ". b:", b)
a += "x"
print("Update a += 'x' ")
print("a ID:", id(a), ". a:", a)
print("b ID:", id(b), ". b:", b)

print("===Use a[:] on 1d list===")
old_list = [1, 2, 3]
new_list = old_list[:]
print('Old List ID:', id(old_list), ". Old List: ", old_list)
print('New List ID:', id(new_list), ". New List: ", new_list)
old_list[1] = 9
print("Update new_list[2][2] = 9")
print('Old List ID:', id(old_list), ". Old List: ", old_list)
print('New List ID:', id(new_list), ". New List: ", new_list)

print("===Use a[:] on 2d list===")
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = old_list[:]
print('Old List ID:', id(old_list), ". Old List: ", old_list)
print('New List ID:', id(new_list), ". New List: ", new_list)
new_list[2][2] = 9
print("Update new_list[2][2] = 9")
print('Old List ID:', id(old_list), ". Old List: ", old_list)
print('New List ID:', id(new_list), ". New List: ", new_list)

print("===Use a[:] on 2d list: correct way===")
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = [item[:] for item in old_list]
print('Old List ID:', id(old_list), ". Old List: ", old_list)
print('New List ID:', id(new_list), ". New List: ", new_list)
new_list[2][2] = 9
print("Update new_list[2][2] = 9")
print('Old List ID:', id(old_list), ". Old List: ", old_list)
print('New List ID:', id(new_list), ". New List: ", new_list)

print("===Use copy.copy ===")
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)
print('Old List ID:', id(old_list), ". Old List: ", old_list)
print('New List ID:', id(new_list), ". New List: ", new_list)
old_list.append([4, 4, 4])
print("Update old_list.append([4, 4, 4]) ")
print('Old List ID:', id(old_list), ". Old List: ", old_list)
print('New List ID:', id(new_list), ". New List: ", new_list)
old_list[1][1] = 100
print("Update old_list[1][1] = 100 ")
print('Old List ID:', id(old_list), ". Old List: ", old_list)
print('New List ID:', id(new_list), ". New List: ", new_list)

print('Old List ID [1][1]:', id(old_list[1][1]))
print('New List ID [1][1]:', id(new_list[1][1]))

print("\n\n")
rows, cols = (5, 5)
arr = [[0]*cols]*rows
print("[[0]*cols]*rows: ", arr)

arr[1][1] = 100
print("arr[1][1] = 100")
print("[[0]*cols]*rows: ", arr)

# arr = [0 for i in range(cols)] * rows
# print("[0 for i in range(cols)] * rows: ", arr)

arr = [[0 for i in range(cols)] for j in range(rows)]
print("[[0 for i in range(cols)] for j in range(rows)]: ", arr)
arr[1][1] = 100
print("arr[1][1] = 100")
print("[[0 for i in range(cols)] for j in range(rows)]: ", arr)
