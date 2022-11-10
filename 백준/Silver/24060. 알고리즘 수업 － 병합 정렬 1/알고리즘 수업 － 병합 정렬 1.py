import sys

N, K  = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))     

count = 0
result = -1

def merge_sort(A, l, r):
    if l < r:
        m = (l + r) // 2
        merge_sort(A, l, m)
        merge_sort(A, m+1, r)
        merge(A, l, m, r)
        
def merge(A, l, m, r):
    global count, result
    i = l
    j = m + 1
    t = 0
    sorting_A = []
    while i <= m and j <= r:
        if A[i] <= A[j]:
            sorting_A.append(A[i])
            i += 1
        else:
            sorting_A.append(A[j])
            j += 1
    
    while i <= m:
        sorting_A.append(A[i])
        i += 1
    
    while j <= r:
        sorting_A.append(A[j])
        j += 1
    
    i = l
    
    while i <= r:
        A[i] = sorting_A[t]
        count += 1
        
        if count == K:
            result = A[i]
            break
        i += 1
        t += 1

merge_sort(A, 0, N - 1)

print(result)