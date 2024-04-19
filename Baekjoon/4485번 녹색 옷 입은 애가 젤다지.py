# 백준 4485번 녹색 옷 입은 애가 젤다지? 문제 (골드4)
# https://www.acmicpc.net/problem/4485


# --- 답안1. 다익스트라 활용 ---
import sys
import heapq
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

problem = 1
while True:
    N = int(input())
    if N == 0:
        break
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    INF = 10 ** 6
    distance = [[INF] * N for _ in range(N)]

    distance[0][0] = graph[0][0]
    q = []
    heapq.heappush(q, (distance[0][0], 0, 0))  # (거리, y, x)

    while q:
        dist, y, x = heapq.heappop(q)  # 거리가 작은 순으로 pop
        if dist > distance[y][x]:
            continue
        # 인접 노드 탐색
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue
            if distance[ny][nx] > dist + graph[ny][nx]:
                distance[ny][nx] = dist + graph[ny][nx]
                heapq.heappush(q, (distance[ny][nx], ny, nx))

    print(f"Problem {problem}: {distance[N - 1][N - 1]}")
    problem += 1


# --- 답안2. BFS & 다익스트라 활용 ---
import sys
import heapq
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x):
    heapq.heappush(heap, (graph[y][x], y, x))
    visited[y][x] = True

    while heap:
        cum_cost, y, x = heapq.heappop(heap)
        if y == N - 1 and x == N - 1:
            return cum_cost

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue
            if not visited[ny][nx]:
                heapq.heappush(heap, (cum_cost + graph[ny][nx], ny, nx))
                visited[ny][nx] = True

problem = 1
while True:
    N = int(input())
    if N == 0:
        break
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    visited = [[False] * N for _ in range(N)]
    heap = []

    answer = bfs(0, 0)
    print(f"Problem {problem}: {answer}")
    problem += 1


# --- 답안3. BFS 같기도하고 다익스트라 같기도한데 안 깔끔한 코드 ---
# import sys
# from collections import deque
# input = sys.stdin.readline
#
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
#
# problem = 1
# q = deque()
# while True:
#     N = int(input())
#     if N == 0:
#         break
#     graph = []
#     for _ in range(N):
#         graph.append(list(map(int, input().split())))
#     distance = [[100000] * N for _ in range(N)]
#
#     y = x = 0
#     distance[y][x] = graph[y][x]
#     q.append((y, x))
#
#     while q:
#         y, x = q.popleft()
#         if y == N - 1 and x == N - 1:
#             continue    # queue에 남아있는 것들을 모두 수행해야하므로 return이 아닌 continue
#
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if ny < 0 or ny >= N or nx < 0 or nx >= N:
#                 continue
#             if distance[ny][nx] > distance[y][x] + graph[ny][nx]:
#                 distance[ny][nx] = distance[y][x] + graph[ny][nx]
#                 q.append((ny, nx))
#
#     print(f"Problem {problem}: {distance[N - 1][N - 1]}")
#     problem += 1