import sys

def quick_sort(A):
    if len(A) <= 1: return A
    pivot = A[0]
    S, M, L = [], [], []
    for a in A:
        if a < pivot:   S.append(a)
        elif a > pivot: L.append(a)
        else:   M.append(a)
    return quick_sort(S) + M + quick_sort(L)

n = int(input())
students = {}

for _ in range(n):
    name , dd, mm, yyyy = sys.stdin.readline().split()
    if (int)(dd) < 10:    dd = '0' + dd
    if (int)(mm) < 10:  mm = '0' + mm
    birth = yyyy + mm + dd
    birth = (int)(birth)
    students[birth] = name

birthList = list(students.keys())

birthList = quick_sort(birthList)

oldest = birthList[0]
youngest = birthList[-1]

print(students[youngest])
print(students[oldest])