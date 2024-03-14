# 백준 2178번 미로 탐색 문제 (실버1)
# https://www.acmicpc.net/problem/2178

'''
BFS 활용 기본 문제.
'''


from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
visited = [[False] * m for _ in range(n)]

d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]


# --- 답안1. 최적의 코드 ---
# 이동 횟수를 graph 값에 저장
def bfs():
    queue = deque([(0, 0)])
    visited[0][0] = True

    while queue:
        row, col = queue.popleft()
        if row == n - 1 and col == m - 1:
            return graph[row][col]
        for i in range(4):
            n_row = row + d_row[i]
            n_col = col + d_col[i]
            if n_row < 0 or n_row >= n or n_col < 0 or n_col >= m:
                continue
            if graph[n_row][n_col] != 0 and not visited[n_row][n_col]:
                visited[n_row][n_col] = True
                graph[n_row][n_col] = graph[row][col] + 1
                queue.append((n_row, n_col))
print(bfs())


# --- 답안2 ---
# 이동 횟수를 queue에 함께 저장
def bfs():
    queue = deque([[0, 0, 1]])
    visited[0][0] = True

    while queue:
        row, col, cnt = queue.popleft()
        if row == n - 1 and col == m - 1:
            return cnt
        for i in range(4):
            n_row = row + d_row[i]
            n_col = col + d_col[i]
            if n_row < 0 or n_row >= n or n_col < 0 or n_col >= m:
                continue
            if graph[n_row][n_col] == 1 and not visited[n_row][n_col]:
                visited[n_row][n_col] = True
                queue.append([n_row, n_col, cnt + 1])
print(bfs())