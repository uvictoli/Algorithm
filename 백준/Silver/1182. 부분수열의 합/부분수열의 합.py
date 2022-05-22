import sys

N, S = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
count = 0

def subset_sum(k, current_sum):
    global count

    if k >= N:
        return

    current_sum += A[k]

    if current_sum == S:
        count += 1

    #A[k]가 선택된 경우
    subset_sum(k + 1, current_sum)

    #A[k]가 선택되지 않은 경우
    subset_sum(k + 1, current_sum - A[k])

subset_sum(0, 0)
print(count)