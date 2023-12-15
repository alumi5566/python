# Example: LC 1101


"""
We are given 10 individuals say, a, b, c, d, e, f, g, h, i, j

Following are relationships to be added:
a <-> b
b <-> d
c <-> f
c <-> i
j <-> e
g <-> j

Given queries like whether a is a friend of d or not. We basically need to create following 4 groups and maintain a quickly accessible connection among group items:
G1 = {a, b, d}
G2 = {c, f, i}
G3 = {e, g, j}
G4 = {h}
"""
def isGroup(lists, x, y):
    def find(i):
        if rootList[i] == i:
            return i
        return find(rootList[i])
    def union(x, y):
        xRoot = find(x)
        yRoot = find(y)
        rootList[yRoot] = xRoot

    rootList = {}
    for list in lists:
        if list[0] not in rootList.keys():
            rootList[list[0]] = list[0]
        if list[1] not in rootList.keys():
            rootList[list[1]] = list[1]
    for list in lists:
        union(list[0], list[1])

    if x not in rootList.keys() or y not in rootList.keys():
        return False

    if find(x) == find(y):
        return True
    return False

relation = [["a", "b"], ["d", "b"], ["c", "f"], ["c", "i"], ["j", "e"], ["g", "j"]]
print(isGroup(relation, "a", "d")) # True
print(isGroup(relation, "a", "h")) # False
print(isGroup(relation, "c", "i")) # True
print(isGroup(relation, "a", "c")) # False

def isGroupPathCompress(lists, x, y):
    def find(i):
        if rootList[i] == i:
            return i
        else:
            # 把i直接指向parent
            parent = find(rootList[i])
            rootList[i] = parent
            return parent
    def union(x, y):
        xRoot = find(x)
        yRoot = find(y)
        if xRoot == yRoot:
            return
        if rankList[xRoot] < rankList[yRoot]:
            rootList[xRoot] = yRoot
        elif rankList[xRoot] > rankList[yRoot]:
            rootList[yRoot] = xRoot
        else:
            rootList[xRoot] = yRoot
            rankList[yRoot] += 1
    rootList = {}
    rankList = {}
    for list in lists:
        if list[0] not in rootList.keys():
            rootList[list[0]] = list[0]
            rankList[list[0]] = 1
        if list[1] not in rootList.keys():
            rootList[list[1]] = list[1]
            rankList[list[1]] = 1
    for list in lists:
        union(list[0], list[1])

    if x not in rootList.keys() or y not in rootList.keys():
        return False

    if find(x) == find(y):
        return True
    return False
print(isGroupPathCompress(relation, "a", "d")) # True
print(isGroupPathCompress(relation, "a", "h")) # False
print(isGroupPathCompress(relation, "c", "i")) # True
print(isGroupPathCompress(relation, "a", "c")) # False