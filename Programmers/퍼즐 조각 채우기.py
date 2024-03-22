# 프로그래머스 퍼즐 조각 채우기 문제 (Lv.3)
# https://school.programmers.co.kr/learn/courses/30/lessons/84021

'''
BFS를 활용하는 심화 문제. 이차원 배열을 자유자재로 변형할 수 있어야 함.

핵심
- table에서 값이 1인것들을 BFS로 찾기
- game_board에서 값이 0인것들을 BFS로 찾기
- 이차원 배열 rotation
'''

from collections import deque


def bfs(graph, x, y, value):
    # value가 0이면 game_board
    # value가 1이면 table

    block = []
    n = len(graph)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(x, y)])
    graph[x][y] = value ^ 1
    block.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == value:
                queue.append((nx, ny))
                graph[nx][ny] = value ^ 1
                block.append((nx, ny))

    return graph, block


def make_arr(block):
    '''
    [(0,0), (0,1), (1,0)]
    ->
    [[1,1],
     [1,0]]
    '''

    all_x, all_y = [], []
    for x, y in block:
        all_x.append(x)
        all_y.append(y)

    max_x, min_x = max(all_x), min(all_x)
    max_y, min_y = max(all_y), min(all_y)
    row = max_x - min_x + 1
    col = max_y - min_y + 1
    arr = [[0] * col for _ in range(row)]

    piece_cnt = 0  # 조각의 칸 수
    for x, y in block:
        arr[x - min_x][y - min_y] = 1
        piece_cnt += 1

    return (arr, piece_cnt)


def rotate(arr):
    row, col = len(arr), len(arr[0])
    rotated_arr = [[0] * row for _ in range(col)]
    for i in range(row):
        for j in range(col):
            rotated_arr[j][row - 1 - i] = arr[i][j]
    return rotated_arr


def solution(game_board, table):
    answer = 0
    n = len(table)
    table_arrays, board_arrays = [], []

    # table에서 값이 1인것들을 BFS로 찾기
    for x in range(n):
        for y in range(n):
            if table[x][y] == 1:
                table, table_block = bfs(table, x, y, value=1)
                table_arrays.append(make_arr(table_block))  # (arr, piece_cnt)

    # game_board에서 값이 0인것들을 BFS로 찾기
    for x in range(n):
        for y in range(n):
            if game_board[x][y] == 0:
                game_board, board_block = bfs(game_board, x, y, value=0)
                board_arrays.append(make_arr(board_block))  # (arr, piece_cnt)

    # table의 조각을 회전시키면서 board에 끼워맞춰보기
    for (table_arr, piece_cnt) in table_arrays:
        is_fit = False
        board_idx = 0
        for (board_arr, _) in board_arrays:
            for _ in range(4):  # 90도, 180도, 270도, 360도 회전
                table_arr = rotate(table_arr)
                if table_arr == board_arr:  # 딱 맞음
                    answer += piece_cnt
                    is_fit = True
                    del board_arrays[board_idx]
                    break
            if is_fit:
                break
            board_idx += 1

    return answer  # 총 채운 조각 수 출력