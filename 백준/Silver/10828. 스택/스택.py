import sys

stack = []
n = int(input())

for _ in range(n):
    command = list(sys.stdin.readline().split())
    if command[0] == "push":
        num = int(command[1])
        stack.append(num)
    elif command[0] == "pop":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack.pop())
    elif command[0] == "top":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack[-1])
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        if len(stack) == 0:    print("1")
        else:    print("0")