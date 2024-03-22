# 백준 2667번 단지번호붙이기 문제 (실버1)
# https://www.acmicpc.net/problem/2667

'''
BFS 활용 문제. (DFS로 풀어도 됨)

visited 배열을 따로 만들어서 구현했었는데, 방문한 곳은 그래프의 값을 0으로 할당하므로 visited를 사용할 필요가 없었다.
단지가 분리되어 있어 BFS를 한번만 수행하면 최대 하나의 단지만 탐색할 수 있다. 따라서 그래프 전체를 탐색해야 하는 점 유의.
'''


from collections import deque

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    graph[x][y] = 0

    cnt = 0  # 단지에 속하는 집의 수
    while queue:
        x, y = queue.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
    return cnt


# 단지의 시작점을 알 수 없으니 그래프 전체를 돌기
houses = []
for x in range(N):
    for y in range(N):
        if graph[x][y] == 1:
            houses.append(bfs(x, y))

# 출력
print(len(houses))
for cnt in sorted(houses):
    print(cnt)