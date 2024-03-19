# 백준 골드4 10282번 해킹 문제
# https://www.acmicpc.net/problem/10282
# 다익스트라 알고리즘 이용

"""
문제에서 '컴퓨터 a가 컴퓨터 b에 의존한다' => '노드 b에 노드 a가 연결되어 있다'
입력에서 '컴퓨터 b가 감염되면 s초 후 컴퓨터 a도 감염된다' => '노드 b에서 노드 a로 가는 거리는 s이다'
입력에서 '해킹당한 컴퓨터의 번호 c' => '시작 노드는 c'
예제에서 2번째 테스트 케이스 입출력을 통해 노드가 감염되기까지 걸리는 시간은 최단 시간으로 구해야 함을 알 수 있음.
출력에서 '총 감염되는 컴퓨터 수' => 최종적으로 방문한 노드의 수
출력에서 '마지막 컴퓨터가 감염되기까지 걸리는 시간' => 최종적으로 방문한 노드 중 가장 큰 거리 값

즉, 한 노드에서 다른 노드들로 가는 최단 거리를 찾는 문제이므로, 다익스트라 알고리즘으로 풀 수 있다!

입력의 수가 많기 때문에 input()을 사용하면 시간 초과 에러가 뜸. sys.stdin.readline()을 사용해야 함.
"""


import heapq
import sys
input = sys.stdin.readline


# --- 답안1. 최적의 답안 ---
test_cases_cnt = int(input())
for _ in range(test_cases_cnt):
    n, d, start_node = map(int, input().split())

    # graph 만들기
    graph = [[] for _ in range(n + 1)]
    for _ in range(d):
        tgt_node, src_node, dist = map(int, input().split())
        graph[src_node].append((dist, tgt_node))

    # distance 배열 만들기
    INF = 999999999
    distance = [INF] * (n + 1)
    distance[start_node] = 0

    # priority queue 만들기
    queue = []
    heapq.heappush(queue, (0, start_node))

    # 다익스트라 알고리즘
    while queue:
        dist, node = heapq.heappop(queue)  # 가장 거리가 짧은 노드
        if dist > distance[node]:
            continue

        for adj_dist, adj_node in graph[node]:
            if dist + adj_dist < distance[adj_node]:  # 최단 거리 업데이트
                distance[adj_node] = dist + adj_dist
                heapq.heappush(queue, (dist + adj_dist, adj_node))

    # 결과 출력 (총 감염된 컴퓨터 수, 총 감염 시간)
    total_cnt, total_time = 0, 0
    for dist in distance[1:]:
        if dist != INF:
            total_cnt += 1
            total_time = max(total_time, dist)
    print(f"{total_cnt} {total_time}")


# --- 답안2. 좀 더 길고 이해가 쉬운 코드 ---
test_cases = []
for _ in range(test_cases_cnt):
    n, d, c = map(int, input().split())

    dependencies = []
    for _ in range(d):
        a, b, s = map(int, input().split())
        dependencies.append((a, b, s))

    test_cases.append({
        "n": n,
        "start": c,
        "dependencies": dependencies,
    })

for case in test_cases:
    n, start_node, dependencies = case["n"], case["start"], case["dependencies"]

    # graph 만들기
    graph = [[] for _ in range(n + 1)]
    for tgt_node, src_node, dist in dependencies:
        graph[src_node].append((dist, tgt_node))

    # distance 배열 만들기
    INF = 999999999
    distance = [INF] * (n + 1)
    distance[start_node] = 0

    # priority queue 만들기
    queue = []
    heapq.heappush(queue, (0, start_node))

    while queue:
        dist, node = heapq.heappop(queue)  # 가장 거리가 짧은 노드
        if dist > distance[node]:
            continue

        for adj_dist, adj_node in graph[node]:
            if dist + adj_dist < distance[adj_node]:  # 최단 거리 업데이트
                distance[adj_node] = dist + adj_dist
                heapq.heappush(queue, (dist + adj_dist, adj_node))

    # 결과 출력 (총 감염된 컴퓨터 수, 총 감염 시간)
    total_cnt, total_time = 0, 0
    for dist in distance[1:]:
        if dist != INF:
            total_cnt += 1
            total_time = max(total_time, dist)
    print(f"{total_cnt} {total_time}")