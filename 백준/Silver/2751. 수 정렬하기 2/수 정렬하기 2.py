import heapq

def heapsort(iterable):
    h = []
    sorted_L = []
    
    for value in iterable:
        heapq.heappush(h, value)
   
    for i in range(len(h)):
        sorted_L.append(heapq.heappop(h))
    return sorted_L


n = int(input())
L = []
for _ in range(n):
    x = int(input())
    L.append(x)
    
sorted_L = heapsort(L)
for x in sorted_L:
    print(x)