# 프로그래머스 월간 코드 챌린지 시즌1 삼각 달팽이 문제 (Lv.2)

'''
아래로 n번 -> 오른쪽으로 (n-1)번 -> 대각선으로 (n-2)번 -> ...
처음에 이걸 파악 못해서 반복문의 범위 지정이 너무 복잡해졌었음.

n=4
1
2 9
3 10 8
4 5  6 7

n=6
1
2 15
3 16 14
4 17 21 13
5 18 19 20 12
6 7  8  9  10 11
'''


def solution(n):
    answer = []

    arr = [[0 for _ in range(n)] for _ in range(n)]  # n x n
    i, j = -1, 0  # 현재 위치
    k = 0
    m = n  # m: n ~ 1 (각 단계에서 연산할 횟수)
    num = 1

    while m > 0:
        # 1단계: 아래로
        for k in range(m):
            arr[i + 1 + k][j] = num
            num += 1
        i = i + 1 + k
        m -= 1

        # 2단계: 오른쪽으로
        for k in range(m):
            arr[i][j + 1 + k] = num
            num += 1
        j = j + 1 + k
        m -= 1

        # 3단계: 대각선
        for k in range(m):
            arr[i - 1 - k][j - 1 - k] = num
            num += 1
        i = i - 1 - k
        j = j - 1 - k
        m -= 1

    # flatten 과정
    # => sum(answer, []) 이렇게 쓸수도 있음
    for i in range(n):
        answer.extend(arr[i][:i + 1])
    return answer