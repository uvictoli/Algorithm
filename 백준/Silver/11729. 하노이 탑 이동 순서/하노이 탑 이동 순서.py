import sys

N = int(sys.stdin.readline())

def hanoi(N, start, by, to):
    if N == 1:  print(start, to)
    else:
        hanoi(N - 1, start, to, by)
        print(start, to)
        hanoi(N - 1, by, start, to)
        
start, by, to = 1, 2, 3
print(2**N - 1)
hanoi(N, start, by, to)