# 백준 1167번 트리의 지름 문제 (골드2)
# https://www.acmicpc.net/problem/1167

'''
BFS 활용 문제.
- 문제에서 말하는 '두 노드 사이의 거리'는 최단 거리를 의미 -> BFS 실행
- 최단 거리들 중에서 가장 긴 것을 반환하면 됨.

BFS를 한번만 실행하면 가장 거리가 긴 경로를 못찾을 수 있기 때문에,
모든 노드에 대해 or 인접노드가 1개인 노드에 대해 시작점으로 설정해서 반복해 실행하니 시간초과가 발생.
책 설명에 따르면 처음 BFS를 실행한 후 가장 거리가 먼 노드를 시작점으로 해서 한번 더 BFS를 실행하라는데 이유가 명확히 이해가 안됐다.
'''


from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n):
    l = list(map(int, input().split()))
    for i in range(1, len(l)-2, 2):
        graph[l[0]].append((l[i], l[i+1]))


# --- 답안1. 최적의 코드. distance 배열을 따로 사용 ---
def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for adj_node, adj_dist in graph[node]:
            if not visited[adj_node]:
                visited[adj_node] = True
                distance[adj_node] = distance[node] + adj_dist
                queue.append(adj_node)

visited = [False] * (n+1)
distance = [0] * (n+1)
bfs(1)
max_dist = max(distance)
max_node = distance.index(max_dist)

visited = [False] * (n+1)
distance = [0] * (n+1)
bfs(max_node)
print(max(max_dist, max(distance)))


# --- 답안2. distance 배열을 따로 사용하지 않고 max_dist, max_node 변수 사용 ---
def bfs(start):
    visited = [False] * (n+1)
    queue = deque([(start, 0)])
    visited[start] = True
    max_dist, max_node = 0, 1
    while queue:
        node, total_dist = queue.popleft()
        if max_dist < total_dist:
            max_dist = total_dist
            max_node = node
        for adj_node, adj_dist in graph[node]:
            if not visited[adj_node]:
                visited[adj_node] = True
                queue.append((adj_node, total_dist + adj_dist))
    return max_dist, max_node

max_dist_1, max_node_1 = bfs(1)
max_dist_2, max_node_2 = bfs(max_node_1)
print(max(max_dist_1, max_dist_2))