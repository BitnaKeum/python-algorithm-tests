# 백준 1197번 최소 스패닝 트리 문제 (골드4)
# https://www.acmicpc.net/problem/1197

'''
최소 신장 트리를 활용하는 기본 문제.
'''


from queue import PriorityQueue
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
queue = PriorityQueue()
for _ in range(E):
    node1, node2, weight = map(int, input().split())
    queue.put((weight, node1, node2))  # weight 기준으로 정렬
parents = list(range(V + 1))


def find(node):
    if node == parents[node]:
        return node
    else:
        parent_node = find(parents[node])
        parents[node] = parent_node
        return parent_node

def union(node1, node2):
    node1_parent = find(node1)
    node2_parent = find(node2)

    if node1_parent <= node2_parent:
        parents[node2_parent] = node1_parent
    else:
        parents[node1_parent] = node2_parent


weight_sum, edge_cnt = 0, 0
while queue.qsize() > 0 and edge_cnt < V-1:
    weight, node1, node2 = queue.get()

    # 사이클 형성 확인
    node1_parent, node2_parent = find(node1), find(node2)
    if node1_parent == node2_parent:  # 연결 X
        continue

    # 두 노드 연결
    union(node1, node2)
    weight_sum += weight
    edge_cnt += 1

print(weight_sum)