import sys

def merge_sort(A):
    if len(A) < 2:  return A
    m = len(A) // 2
    S = merge_sort(A[:m]) #low_arr
    L = merge_sort(A[m:]) #high_arr

    merged = []
    s = l = 0
    while s < len(S) and l < len(L):
        if S[s] < L[l]:
            merged.append(S[s])
            s += 1
        else:
            merged.append(L[l])
            l += 1

    merged += S[s:]
    merged += L[l:]
    return merged


n, h = map(int, sys.stdin.readline().split())
fruits = list(map(int, sys.stdin.readline().split()))

merged_fruits = merge_sort(fruits)

if h < merged_fruits[0]:    print(h)
else:
    for fruit in merged_fruits:
        if fruit <= h:  h += 1
    print(h)