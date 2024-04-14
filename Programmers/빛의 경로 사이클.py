# 프로그래머스 월간 코드 챌린지 시즌3 빛의 경로 사이클 문제 (Lv.2)
# https://school.programmers.co.kr/learn/courses/30/lessons/86052

'''
그래프 탐색 문제인데, 방향을 재설정하고 범위 이외 부분을 처리해야 하는 세부적인 구현이 필요한 문제.
내가 놓친 부분:
- visited 배열을 3차원으로 만드는 것을 떠올리지 못했음
- 마지막에 오름차순으로 정렬해서 출력하라는 부분을 놓침
- 시작 위치는 무조건 (0, 0)인 것으로 잘못 이해했음
'''


def get_d(ch, d):  # 다음 방향 찾기
    if ch == 'L':   # ex: [0,1,2,3] -> [-4,-3,-2,-1]
        d -= 1
        if d < 0:
            d += 4
    elif ch == 'R': # ex: [0,1,2,3] -> [4,5,6,7]
        d += 1
        if d >= 4:
            d -= 4
    return d


def move(y, x, d):
    y += dy[d]
    x += dx[d]

    # 범위 밖 처리하기
    if y == -1:
        y = row - 1
    elif y == row:
        y = 0
    if x == -1:
        x = col - 1
    elif x == col:
        x = 0

    return y, x


def solution(grid):
    global row, col, dy, dx

    answer = []
    grid = [list(s) for s in grid]
    row, col = len(grid), len(grid[0])
    visited = [[[False] * 4 for _ in range(col)] for _ in range(row)]  # row * col * 4
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    # d: ['UP', 'RIGHT', 'DOWN', 'LEFT']

    for y_init in range(row):
        for x_init in range(col):
            for d_init in range(4):
                y, x, d = y_init, x_init, d_init
                cycle_len = 0
                while not visited[y][x][d]:
                    visited[y][x][d] = True  # 방문 처리

                    d = get_d(grid[y][x], d)
                    y, x = move(y, x, d)
                    cycle_len += 1
                if cycle_len > 0 and (y, x, d) == (y_init, x_init, d_init):
                    answer.append(cycle_len)

    return sorted(answer)