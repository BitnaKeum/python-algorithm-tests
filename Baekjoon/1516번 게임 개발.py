# 백준 1516번 게임 개발 문제 (골드3)
# https://www.acmicpc.net/problem/1516

'''
각 건물을 짓는 데에는 순서가 있음. 이 순서를 정렬해서 총 시간을 구하는 문제.
=> 노드의 순서를 정렬하는 위상 정렬 알고리즘을 사용하면 되겠다!

2번을 지으려면 1번을 먼저 지어야함 => 1번이 2번 가리킴
graph
1 -> 2,3,4
2 ->
3 -> 4,5
4 ->
5 ->

line 47이 이해 안되서 미해결.
'''


from collections import deque

n = int(input())  # 건물의 종류 수
times = [0] * (n + 1)  # 각 건물 짓는 시간
final_times = [0] * (n + 1)  # 최종적인 각 건물 짓는 시간
indegree = [0] * (n + 1)  # 나를 가리키는 엣지의 수
graph = [[] for _ in range(n + 1)]

for cur_node in range(1, n + 1):
    splits = list(map(int, input().split()))
    times[cur_node] = splits[0]
    for prev_node in splits[1:-1]:
        graph[prev_node].append(cur_node)
        indegree[cur_node] += 1

queue = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    cur_node = queue.popleft()
    for next_node in graph[cur_node]:
        indegree[next_node] -= 1

        # 다른 경로로부터 계산된 값과 현재 경로에서 계산된 값 중 더 큰 걸로 할당
        # 최소 시간을 구하라고 했는데 왜 더 큰걸로 하지?
        final_times[next_node] = max(final_times[next_node], final_times[cur_node] + times[cur_node])

        if indegree[next_node] == 0:
            queue.append(next_node)

for i in range(1, n + 1):
    final_times[i] += times[i]
    print(final_times[i])