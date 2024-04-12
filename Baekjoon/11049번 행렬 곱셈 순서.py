# 백준 11049번 행렬 곱셈 순서 문제 (골드3)
# https://www.acmicpc.net/problem/11049

'''
미통과. 손도 못댔다ㅠ

Python3으로 하면 아무리 해도 시간초과 발생. Pypy3으로 컴파일해야함.

풀이:

점화식:
D[i][j]: i~j까지의 구간에서 하나의 행렬로 만드는 최소 연산 횟수

이미 방문한 구간 => return D[i][j]
구간 내에 행렬이 1개 => D[i][j] = 0
구간 내에 행렬이 2개 => D[i][j] = row_i * row_j * col_j
구간 내에 행렬이 3개 이상 => 재귀적으로 쪼개서 가장 작은 결과값 사용
    for k in range(i, j):
       value = recursion(D[i][k]) + recursion(D[k+1][j]) + (row_i * col_k * col_j))
       if value < min_value:
           min_value = value
'''


import sys
input = sys.stdin.readline

N = int(input())
matrixes = []
for _ in range(N):
    row, col = map(int, input().split())
    matrixes.append((row, col))
D = [[-1 for _ in range(N)] for _ in range(N)]  # N * N


def recursion(i, j):
    if D[i][j] != -1:  # 이미 방문한 경우
        return D[i][j]

    if i == j:  # 구간 내에 행렬이 1개
        D[i][j] = 0
    elif j == i + 1:  # 구간 내에 행렬이 2개
        D[i][j] = matrixes[i][0] * matrixes[j][0] * matrixes[j][1]  # row_i * row_j * col_j
    else:
        min_value = sys.maxsize
        for k in range(i, j):
            value = recursion(i, k) + recursion(k + 1, j) + (matrixes[i][0] * matrixes[k][1] * matrixes[j][1])  # recursion() + recursion() + (row_i * col_k * col_j))
            if value < min_value:
                min_value = value
        D[i][j] = min_value
    return D[i][j]

print(recursion(0, N - 1))