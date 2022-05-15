import heapq
import sys

def heapsort(iterable):
    h = []
    sorted_L = []

    for value in iterable:
        heapq.heappush(h, value)

    for _ in range(len(h)):
        sorted_L.append(heapq.heappop(h))
    return sorted_L


N, L, H = map(int, sys.stdin.readline().split())
scores = list(map(int, sys.stdin.readline().split()))

sorted_scores = heapsort(scores)
H = N - H
considered_scores = sorted_scores[L : H]
#print(considered_scores)

grade = sum(considered_scores) / len(considered_scores)
print(grade)