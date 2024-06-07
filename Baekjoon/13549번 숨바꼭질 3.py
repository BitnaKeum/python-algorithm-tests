# 백준 13549번 숨바꼭질 3 문제 (골드5)
# https://www.acmicpc.net/problem/13549


'''
두번 풀었는데 두번 다 재귀로 접근해서 RecursionError로 틀림.
첫 시도엔 BFS (appendleft() 사용)로 풀었고
두번째 시도엔 BFS라는 힌트를 얻었다가, 가중치 값이 균일하지 않고 간선의 최소 합이 아닌 가중치의 최소 합을 구해야하는 것을 깨닫고 다익스트라로 풀었음.
'''

# --- 코드1. 최적의 코드. 다익스트라 이용 ---
import heapq

N, K = map(int, input().split())

heap = [(0, N)]  # (time, node)
heapq.heapify(heap)
distance = [1000000] * 100001
distance[N] = 0
while heap:
    time, node = heapq.heappop(heap)
    if time > distance[node]:
        continue

    for adj_node, adj_time in [(node * 2, 0), (node + 1, 1), (node - 1, 1)]:
        if 0 <= adj_node <= 100000 and distance[adj_node] > time + adj_time:
            heapq.heappush(heap, (time + adj_time, adj_node))
            distance[adj_node] = time + adj_time

    # 위 for문 (line 25~28)을 풀어서 쓴 코드 (line 31~39)
    # if 0 <= node * 2 <= 100000 and distance[node * 2] > time:      # 순간 이동 (X*2)
    #     heapq.heappush(heap, (time, node * 2))
    #     distance[node * 2] = time
    # if 0 <= node + 1 <= 100000 and distance[node + 1] > time + 1:  # 걷기 (X+1)
    #     heapq.heappush(heap, (time + 1, node + 1))
    #     distance[node + 1] = time + 1
    # if 0 <= node - 1 <= 100000 and distance[node - 1] > time + 1:  # 걷기 (X-1)
    #     heapq.heappush(heap, (time + 1, node - 1))
    #     distance[node - 1] = time + 1

print(distance[K])


# --- 코드2. BFS 이용 + appendleft() ---
# 최소 시간 (= 최단 거리) 찾는 문제이므로, BFS를 활용해 풀 수 있음
# 순간 이동은 가중치가 더 작기 때문에 우선순위를 높여야함 => queue에 추가할때 append() 대신 appendleft()를 사용
# deque 대신 PriorityQueue를 사용해봤지만 속도가 매우 느려짐

from collections import deque

N, K = map(int, input().split())
if N >= K:
    print(N - K)
else:
    queue = deque([(N, 0)])
    MAX = 100001
    visited = [MAX] * MAX
    while queue:
        num, time = queue.popleft()
        if num >= MAX or num < 0:
            continue
        if visited[num] > time:
        #if visited[num] == MAX:    # 이렇게 작성해도 ok
            visited[num] = time
            # 순간 이동
            queue.appendleft((2 * num, time))
            # 걷기
            queue.append((num - 1, time + 1))
            queue.append((num + 1, time + 1))
    print(visited[K])