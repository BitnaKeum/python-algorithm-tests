# 백준 7682번 틱택토 문제 (골드5)
# https://www.acmicpc.net/problem/7682


import sys
input = sys.stdin.readline


def get_winner():
    x_winner, o_winner = False, False

    def is_win(s):
        nonlocal x_winner, o_winner
        if s == 'XXX':
            x_winner = True
        elif s == 'OOO':
            o_winner = True

    for i in range(3):  # 가로
        is_win(''.join(board[i]))
    for j in range(3):  # 세로
        is_win(''.join([board[i][j] for i in range(3)]))
    # 대각선
    is_win(''.join([board[i][i] for i in range(3)]))
    is_win(''.join([board[i][2-i] for i in range(3)]))

    return x_winner, o_winner


while True:
    line = input().rstrip()
    if line == 'end':
        break
    x_cnt, o_cnt = line.count('X'), line.count('O')
    # X의 개수는 O의 개수와 같거나 +1 여야함
    if x_cnt < o_cnt or x_cnt > o_cnt + 1:
        print('invalid')
        continue

    board = [list(line[i*3:i*3+3]) for i in range(3)]
    x_winner, o_winner = get_winner()
    if x_winner and o_winner:
        print('invalid')
    elif (o_winner and x_cnt == o_cnt) or (x_winner and x_cnt == o_cnt + 1):
        # O가 이겼을 때, X의 개수 == O의 개수 여야함
        # X가 이겼을 때, X의 개수 = O의 개수 + 1 여야함
        print('valid')
    elif (x_cnt + o_cnt == 3*3) and not x_winner and not o_winner:
        # 게임판이 가득 차고 승부가 안난 경우
        print('valid')
    else:
        print('invalid')