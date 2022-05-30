#큐가 빌 때까지 루프를 돌면서 큐에서 하나씩 꺼내 연결된 노드들을 탐색

from collections import deque
import sys

def BFS():
    q = deque([(0, 0)])
    answer = float("inf")
    visited[0][0] = 1

    while q:
        x, y = q.popleft()

        if graph[x][y] == 2:
            answer = abs(N - 1 - x) + abs(M - 1 - y) + visited[x][y] - 1

        if (x, y) == (N - 1, M - 1):
            answer = min(visited[x][y] - 1, answer)
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                if graph[nx][ny] != 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

    return answer

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M, T = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

count = BFS()
if 0 < count <= T:
    print(count)
else:
    print("Fail")
