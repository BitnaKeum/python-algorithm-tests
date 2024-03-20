# 백준 1854번 K번째 최단경로 찾기 문제 (플래티넘4)
# https://www.acmicpc.net/problem/1854

'''
다익스트라 알고리즘 활용 심화 문제.
'''


import heapq
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

INF = 10 ** 6
distance = [[INF] * k for _ in range(n + 1)]    # distance 배열을 이차원으로 만들기

queue = []
start = 1
heapq.heappush(queue, (0, start))  # (거리, 노드)
distance[start][0] = 0

while queue:
    dist, node = heapq.heappop(queue)  # 가장 거리가 짧은 노드

    for adj_node, adj_dist in graph[node]:
        new_dist = dist + adj_dist
        if new_dist < distance[adj_node][k - 1]:    # k번째로 작은 거리와 비교
            distance[adj_node][k - 1] = new_dist    # 거리 업데이트
            distance[adj_node].sort()
            heapq.heappush(queue, (new_dist, adj_node))

for i in range(1, n + 1):
    if distance[i][k - 1] == INF:
        print(-1)
    else:
        print(distance[i][k - 1])