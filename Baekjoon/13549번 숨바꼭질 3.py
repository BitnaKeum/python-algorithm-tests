# 백준 13549번 숨바꼭질 3 문제 (골드5)
# https://www.acmicpc.net/problem/13549

'''
미통과. 재귀로 구현해서 RecursionError가 발생했음.

핵심:
- 최소 시간 (= 최단 거리) 찾는 문제이므로 BFS를 활용해 풀 수 있다.
- 순간 이동은 가중치가 더 적기 때문에 우선순위를 높여야함. 그래서 queue에 추가할때 append() 대신 appendleft()를 사용해야한다.
  - deque 대신 PriorityQueue를 사용해봤는데 속도가 너무 느려져서 deque를 쓰는 것이 나음.

걷기: 가중치 1
순간 이동: 가중치 0
'''

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