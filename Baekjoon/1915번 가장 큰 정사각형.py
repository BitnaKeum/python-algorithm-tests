# 백준 1915번 가장 큰 정사각형 문제 (골드4)
# https://www.acmicpc.net/problem/1915


'''
미통과. Dynamic Programming 활용 문제.
엄청 복잡하게 푸는 방법만 떠올렸는데 풀이는 너무 간단해서 놀랐다. DP 어렵다ㅜㅜ

풀이:

D[i][j]: i행 j열이 오른쪽아래 꼭짓점일때 가능한 정사각형의 크기

핵심: 값이 0보다 큰 칸에 대해, 위쪽/왼쪽/왼쪽위대각선 칸 중 가장 작은 값 + 1을 저장

점화식:
D[i][j] = min(D[i-1][j], D[i][j-1], D[i-1][j-1]) + 1 (D[i][j]!=0 일때)
D[i][j] = 0 (D[i][j]==0 일때)

예시1
0 1 0 0
0 1 1 1
1 1 1 0
0 0 1 0
->
0 1 0 0
0 1 1 1
1 1 2 0
0 0 1 0

예시2
0 1 0 0 0
0 1 1 0 0
1 1 1 1 1
0 0 1 1 1
0 0 1 1 1
->
0 1 0 0 0
0 1 1 0 0
1 1 2 1 1
0 0 1 2 2
0 0 1 2 3
'''


n, m = map(int, input().split())
D = []
for _ in range(n):  # n x m
    D.append(list(map(int, input())))

answer = 0
for i in range(1, n):
    for j in range(1, m):
        if D[i][j] != 0:
            D[i][j] = min(D[i - 1][j], D[i][j - 1], D[i - 1][j - 1]) + 1
            if D[i][j] > answer:
                answer = D[i][j]

print(answer ** 2)