# 백준 1260번 문제 DFS와 BFS (실버2)
# https://www.acmicpc.net/problem/1260

'''
DFS와 BFS를 구현하는 기본 문제.
2년전에 작성한 코드와 비교해보니 훨씬 간결하게 작성하여서 실력 성장을 체감할 수 있었다!
'''


# --- 답안1. 최적의 답안 ---
from collections import deque
import sys
sys.setrecursionlimit(10000)

def dfs(node):
    print(node, end=" ")
    visited[node] = True
    for adj_node in graph[node]:
        if not visited[adj_node]:
            dfs(adj_node)

def bfs(node):
    queue = deque([node])
    visited[node] = True
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for adj_node in graph[node]:
            if not visited[adj_node]:
                queue.append(adj_node)
                visited[adj_node] = True

n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)
for idx in range(1, n + 1):  # 중복 제거
    graph[idx] = sorted(list(set(graph[idx])))

# DFS
visited = [False] * (n + 1)
dfs(start)
print()

# BFS
visited = [False] * (n + 1)
bfs(start)


# --- 답안2. 2년전에 작성한 비효율적인 코드 ---
# from collections import deque
#
# def dfs():
#     visit = {}
#     stack = [V]
#     while stack:
#         node = stack.pop()
#         if node not in visit:
#             visit[node] = True
#             stack.extend(reversed(sorted(list(graph[node] - set(visit.keys())))))
#     return ' '.join(str(key) for key in visit.keys())
#
# def bfs():
#     visit = {}
#     queue = deque([V])
#     while queue:
#         node = queue.popleft()
#         if node not in visit:
#             visit[node] = True
#             queue.extend(sorted(list(graph[node] - set(visit.keys()))))
#     return ' '.join(str(key) for key in visit.keys())
#
#
# N, M, V = map(int, input().split())
#
# graph = [set() for _ in range(N + 1)]
# for _ in range(M):
#     num1, num2 = map(int, input().split())
#     graph[num1].add(num2)
#     graph[num2].add(num1)
#
# print(dfs())
# print(bfs())
