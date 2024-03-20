# 백준 1753번 최단경로 문제 (골드4)
# https://www.acmicpc.net/problem/1753


'''
다익스트라 알고리즘 활용 문제.
'''


import sys
input = sys.stdin.readline
from queue import PriorityQueue  # 가장 거리가 짧은 노드를 반환하기 위해서 우선순위큐 사용

V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, dist = map(int, input().split())
    graph[u].append((v, dist))

INF = 10 ** 6
distance = [INF] * (V + 1)
queue = PriorityQueue()

# 시작 노드 처리
queue.put((0, start))  # (거리, 노드) 순으로 저장
distance[start] = 0

while queue.qsize() > 0:
    dist, node = queue.get()  # 거리가 가장 작은 노드를 반환
    if dist > distance[node]:  # invalid
        continue
    for adj_node, adj_dist in graph[node]:
        if dist + adj_dist < distance[adj_node]:
            distance[adj_node] = dist + adj_dist        # 최단 거리 업데이트
            queue.put((distance[adj_node], adj_node))   # (거리, 노드) 순으로 저장

for i in range(1, V + 1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])