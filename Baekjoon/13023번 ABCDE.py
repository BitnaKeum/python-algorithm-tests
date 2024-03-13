# 백준 13023번 ABCDE 문제 (골드5)
# https://www.acmicpc.net/problem/13023

'''
DFS 활용 문제.
문제 이해가 좀 어려웠는데, 쉽게 말해 depth가 5인 경로가 존재하는지를 찾는 문제이다.
풀이가 거의 정확했으나 인접노드 탐색이 끝난 후에 현재 노드 방문여부를 False로 설정(line 29)하는 것을 간과해서 틀림.
'''

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * n
answer = False

def dfs(node, depth):
    global answer
    visited[node] = True
    if depth >= 5:
        answer = True
        return
    for adj_node in graph[node]:
        if not visited[adj_node]:
            dfs(adj_node, depth+1)
            if answer:
                break
    visited[node] = False # 요게 중요

for start in range(n):
    if dfs(start, 1):
        break
print(int(answer))