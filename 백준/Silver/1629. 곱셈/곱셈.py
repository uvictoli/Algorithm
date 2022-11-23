import sys
user_in = sys.stdin.readline()

A, B, C = map(int, user_in.split())

def power(A, B):
    if B == 1:
        return A % C
    
    temp = power(A, B // 2)
    if B % 2 == 0:
        return (temp * temp) % C
    else:
        return (temp * temp * A) % C
    

print(power(A, B))