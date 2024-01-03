# Using a list, every operation is O(nlogn)
list_pq = []

list_pq.append((2, "two"))
list_pq.sort(reverse=True)
list_pq.append((3, "three"))
list_pq.sort(reverse=True)
list_pq.append((1, "one"))
list_pq.sort(reverse=True)
list_pq.append((4, "four"))
list_pq.sort(reverse=True)
while list_pq:
    print(list_pq.pop(0), end="")
print("\n")
# Using heapq, default headq only support min heap
import heapq
heap_pq = []
heapq.heappush(heap_pq, (2, "two"))
heapq.heappush(heap_pq, (3, "three"))
heapq.heappush(heap_pq, (1, "bbb"))
heapq.heappush(heap_pq, (1, "aaa"))
heapq.heappush(heap_pq, (4, "four"))
heapq.heappush(heap_pq, (4, "aaa"))
while heap_pq:
    print(heapq.heappop(heap_pq), end="")
print("\n")

# using QUEUE.PRIORITYQUEUE
from queue import PriorityQueue
pq = PriorityQueue()
pq.put((2, "two"))
pq.put((3, "three"))
pq.put((1, "one"))
pq.put((4, "four"))
while pq.qsize() != 0:
    print(pq.get(), end="")
print("\n")

pq.put(-2, (2, "two"))
pq.put(-3, (3, "three"))
pq.put(-1, (1, "one"))
pq.put(-4, (4, "four"))
while pq.qsize() != 0:
    print(pq.get(), end="")
print("\n")