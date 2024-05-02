# 백준 14940번 쉬운 최단거리 문제 (실버1)
# https://www.acmicpc.net/problem/14940

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 2 -> 0, 1 -> -1, 0 -> 0
for y in range(n):
    for x in range(m):
        if graph[y][x] == 2:
            target = (y, x)
            graph[y][x] = 0
        elif graph[y][x] == 1:
            graph[y][x] = -1

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
q = deque()
q.append(target)
graph[target[0]][target[1]] = 0
while q:
    y, x = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= n or nx < 0 or nx >= m or graph[ny][nx] == 0:
            continue
        if graph[ny][nx] == -1: # 미방문
            q.append((ny, nx))
            graph[ny][nx] = graph[y][x] + 1

for row in graph:
    print(*row)