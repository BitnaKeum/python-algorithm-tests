# 백준 10844번 쉬운 계단 수 문제 (실버1)
# https://www.acmicpc.net/problem/10844


'''
처음에 경우의 수를 세는 데에만 집중해서 접근했음
 -> 0 or 9일 때는 이전 경우의 수 그대로, 1~8일 때는 이전 경우의 수 * 2로 점화식을 세움
    but, 현재 자리 값이 뭔지에 따라서 그 다음 경우의 수가 분기됨
    따라서 경우의 수만 구하는 것이 아니라, 각 자리의 각 값마다 경우의 수를 구하도록 접근해야 함 (이차원 배열로)


N==1, 1~9
N==2, 10,12, 21,23, 32,34, 43,45, 54,56, 65,67, 76,78, 87,89, 98
 => 0과 9는 인접 수 1개
    1,2,3,4,5,6,7,8은 인접 수 2개

점화식
D[n][j] = D[n-1][j+1]    # j==0
D[n][j] = D[n-1][j-1]    # j==9
D[n][j] = D[n-1][j-1] + D[n-1][j+1]    # 1<=j<=8
'''


# --- 최적의 답안 ---

n = int(input())
mod = 1000000000

D = [[0] * 10 for _ in range(n+1)]    # (n+1) x 10
for j in range(1, 10):     # i: 1, j: 1 ~ 9
    D[1][j] = 1
for i in range(2, n+1):    # i: 2 ~ n
    for j in range(10):    # j: 0 ~ 9
        if j == 0:
            D[i][j] = D[i-1][j+1] % mod
        elif j == 9:
            D[i][j] = D[i-1][j-1] % mod
        else:
            D[i][j] = (D[i-1][j-1] + D[i-1][j+1]) % mod
print(sum(D[n]) % mod)