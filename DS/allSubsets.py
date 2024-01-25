

def dfs(i):
    if i == len(array):
        res.append(subset[:])
        return
    subset.append(array[i])
    dfs(i+1)
    subset.pop()
    dfs(i+1)


array = [1, 2, 3]
res = []
subset = []
dfs(0)
# subsets(array)
print(res)
