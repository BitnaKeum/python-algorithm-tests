# 백준 11657번 타임머신 문제 (골드4)
# https://www.acmicpc.net/problem/11657

'''
벨만-포드 알고리즘을 활용하는 기본 문제.
'''


import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 엣지 리스트, distance 리스트 만들기
graph = []
for _ in range(m):
    a, b, dist = map(int, input().split())
    graph.append((a, b, dist))
INF = 10 ** 10  # 보통은 10 ** 6으로 사용하는데 이 문제에서는 그러면 출력 초과 에러가 발생해서 증가시켰다.
distance = [INF] * (n + 1)

distance[1] = 0

for _ in range(n - 1):
    for (a, b, dist) in graph:
        if distance[a] != INF and distance[a] + dist < distance[b]:
            distance[b] = distance[a] + dist

# 음수 사이클 확인
neg_cycle = False
for (a, b, dist) in graph:
    if distance[a] != INF and distance[a] + dist < distance[b]:
        neg_cycle = True

if neg_cycle:  # 시간을 무한히 오래 전으로 되돌릴 수 있는 경우
    print(-1)
else:
    for i in range(2, n + 1):
        if distance[i] != INF:
            print(distance[i])
        else:
            print(-1)