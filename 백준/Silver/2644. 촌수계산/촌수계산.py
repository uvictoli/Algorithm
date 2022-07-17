n = int(input())
p1, p2 = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = []

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v, num):
    num += 1
    visited[v] = True

    if v == p2:
        result.append(num)

    for i in graph[v]:
        if not visited[i]:
            dfs(i, num)


dfs(p1, 0)
if len(result) == 0:
    print(-1)
else:
    print(result[0] - 1)