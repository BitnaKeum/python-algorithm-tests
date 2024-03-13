# 백준 11724번 연결 요소의 개수 문제 (실버2)
# https://www.acmicpc.net/problem/11724

'''
DFS 활용 문제.
핵심 풀이는 정확히 떠올렸으나 예외처리를 하려다 시간초과가 발생함.
재귀로 풀이 시 setrecursionlimit()를 꼭 설정해주자.
'''

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    #if v not in graph[u]:
    graph[u].append(v)
    #if u not in graph[v]:
    graph[v].append(u)
visited = [False] * (n+1)

def dfs(graph, node, visited):
    visited[node] = True
    for adj_node in graph[node]:
        if not visited[adj_node]:
            dfs(graph, adj_node, visited)

answer = 0
for node in range(1, n+1):
    if not visited[node]:
        dfs(graph, node, visited)
        answer += 1
print(answer)