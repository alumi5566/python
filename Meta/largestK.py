import heapq

# https://www.1point3acres.com/bbs/thread-1045820-1-1.html
# Find largest k number in array
arr = [2, 1, 4, 3, 5, 9, 8, 0, 1, 3, 2, 5]
k = 6
# out
# 1 = sort and get the first k element (O(nlogn))
# _arr = sorted(arr, reverse=True)
out1 = sorted(arr, reverse=True)[0:k]
print("1 = ", out1)

# 2 = heap (O(nlogk))
hp = []
for a in arr:
    if len(hp) < k:
        heapq.heappush(hp, a)
    else:
        if a > hp[0]:
            heapq.heappop(hp)
            heapq.heappush(hp, a)
print("2 = ", hp)

# 3 = quick select
def getLargestK(array, k):
    if len(array) == k:
        return array
    pivot = array[k]
    lhs, rhs = [], []
    for a in array:
        if a >= pivot:
            lhs.append(a)
        else:
            rhs.append(a)
    print(lhs)
    print(rhs)
    if len(lhs) >= k:
        return getLargestK(lhs, k)
    else:
        return lhs + getLargestK(rhs, k - len(lhs))
print("3 = " + getLargestK(arr, k))