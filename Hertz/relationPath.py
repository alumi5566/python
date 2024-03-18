import collections
from functools import cache


# input = ["Lucas", "Ava"]
def findPath(arr, input):
    graph = collections.defaultdict(set)
    for a in arr:
        graph[a[0]].add(a[1])
    # print(graph)
    @cache
    def dfs(root, p2):
        if root == p2:
            return True, [root]
        if len(graph[root]) == 0:
            return False, []
        ret = []
        ret.append(root)
        for next in graph[root]:
            res = dfs(next, p2)
            if res[0]:
                # print(root, res[1], "len:", len(res[1]))
                ret.extend(res[1])
            return True, ret
        # print(ret, "len:", len(ret))
        return False, []
    ret = dfs(input[0], input[1])
    relation = ret[1]
    if len(relation) == 0:
        relation = dfs(input[1], input[0])[1]
        print(relation)
        for i in range(len(relation)-1, 0, -1):
            print(relation[i], "was invited by", relation[i-1])
    else:
        print(relation)
        for i in range(len(relation)-1):
            print(relation[i], "invited", relation[i+1])

arr = [
    ["Ava", "Mia"],
    ["Mia", "Oliver"],
    ["Mia", "Lucas"]
]
input = ["Ava", "Lucas"]
findPath(arr, input)
input2 = ["Lucas", "Ava"]
findPath(arr, input2)