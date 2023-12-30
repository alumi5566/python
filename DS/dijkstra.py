import collections
import heapq
from heapq import heappush, heappop
from typing import List

def find(graph, x, y, d):
    if (x, y) in d:
        return d[(x, y)]
    pq, visit = [], set()
    heapq.heappush(pq, (0, x))
    while pq:
        cost, node = heapq.heappop(pq)
        if node == y:
            return cost
        if node in visit:
            continue
        visit.add(node)
        for nei, new_cost in graph[node]:
            heapq.heappush(pq, (cost+new_cost, nei))
    return -1


def minimumCost(source, target, original, changed, cost):
    n = len(source)
    # Learn the way to store the graph
    graph = collections.defaultdict(list)
    for x,y,z in zip(original, changed, cost):
        graph[x].append([y, z])

    res, d = 0, {}
    for i in range(n):
        val = find(graph, source[i], target[i], d)
        if val == -1:
            return -1
        else:
            res += val
        d[(source[i], target[i])] = val

    return res
# print(minimumCostCY("abcd", "acbe", ["a","b","c","c","e","d"], ["b","c","b","e","b","e"], [2,5,5,1,2,20]))
print(minimumCost("abcd", "acbe", ["a","b","c","c","e","d"], ["b","c","b","e","b","e"], [2,5,5,1,2,20]))

