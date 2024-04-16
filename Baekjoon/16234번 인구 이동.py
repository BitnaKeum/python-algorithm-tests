# 백준 16234번 인구 이동 문제 (골드4)
# https://www.acmicpc.net/problem/16234

'''
처음에 구현한 알고리즘:
1. 반복문을 통해 오른쪽/아래 칸에 대해 차이가 gap_min 이상 gap_max 이하면 visited에 현재 칸과 오른쪽/아래 칸을 1로 할당
2. visited==1인 칸의 인구 수를 모두 더한 다음 칸 수로 나눠서 연합 인구 수 구하기
3. visited==1인 칸에 대해 A 배열의 값을 연합 인구 수로 재할당

그런데 위 알고리즘은 연합이 2개 이상인 경우를 커버하지 못함.
-> 그래서 2번, 3번 단계에 BFS를 추가해 각 연합마다 계산하도록 수정함.

그런데 이렇게하니 메모리 초과 에러 발생.
-> 그래서 1번 단계를 별도로 수행하지 않고 BFS 과정에 통합하도록 수정함.

그런데 이번에는 시간 초과 에러 발생.
사유: line 56~58을 line 47 아래에 작성했었는데, 이렇게 되면 이미 queue에 집어넣은 값이 방문 처리가 안되어있기 때문에 이 값이 queue에 여러번 들어가면서 시간 초과가 발생하는 것임.
-> 그래서 조건을 만족했을 때 queue에 집어넣은 직후에 수행하도록 수정함.


p.s.
삼성SW역량테스트 문제라고 하던데, 그런만큼 구현 과정이 꽤 빡세게 느껴졌다.
하지만 BFS에서 visited==False 조건뿐 아니라 추가적인 조건을 사용하는 법을 익힐 수 있었던 좋은 BFS 활용 문제였다.
나중에 다시 풀어보면 좋을듯!
'''


from collections import deque
import sys
input = sys.stdin.readline

N, gap_min, gap_max = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
q = deque()
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(y, x):
    # 시작 값
    q.append((y, x))
    visited[y][x] = True
    p_sum = A[y][x]
    union = [(y, x)]

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= N or nx < 0 or nx >= N:  # 범위 밖
                continue
            if not visited[ny][nx] and gap_min <= abs(A[y][x] - A[ny][nx]) <= gap_max:
                q.append((ny, nx))
                visited[ny][nx] = True
                p_sum += A[ny][nx]
                union.append((ny, nx))

    if len(union) > 1:  # 인구 이동 O
        p_new = p_sum // len(union)
        for y, x in union:
            A[y][x] = p_new
        return 1
    else:  # 인구 이동 X
        return 0


answer = 0
while True:
    visited = [[False for _ in range(N)] for _ in range(N)]
    res = 0
    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                res += bfs(y, x)
    if res == 0:
        break
    answer += 1
print(answer)