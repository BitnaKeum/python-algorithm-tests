# 백준 5972번 택배 배송 문제 (골드5)
# https://www.acmicpc.net/problem/5972

'''
1번 노드에서 N번 노드로 가는 최단 거리를 찾아야함. 노드 간 가중치는 서로 다름.
=> 기본적인 다익스트라 활용 문제.
'''


from queue import PriorityQueue
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    node1, node2, weight = map(int, input().split())
    graph[node1].append((node2, weight))
    graph[node2].append((node1, weight))
q = PriorityQueue()
distance = [10 ** 8] * (N+1)

q.put((0, 1))
distance[1] = 0
while q.qsize() > 0:
    dist, node = q.get()
    if distance[node] < dist:
        continue
    for adj_node, weight in graph[node]:
        if distance[adj_node] > dist + weight:
            distance[adj_node] = dist + weight
            q.put((distance[adj_node], adj_node))
print(distance[N])