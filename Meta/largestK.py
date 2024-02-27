# https://www.1point3acres.com/bbs/thread-1045820-1-1.html
# Find largest k number in array
arr = [2, 1, 4, 3, 5, 9, 8, 0, 1, 3, 2, 5]
k = 6
# out
# 1 = sort and get the first k element (O(nlogn))
# _arr = sorted(arr, reverse=True)
out1 = sorted(arr, reverse=True)[0:k]
print(out1)

# 2 =