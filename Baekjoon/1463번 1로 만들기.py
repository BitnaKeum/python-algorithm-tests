# 백준 1463번 1로 만들기 문제 (실버3)
# https://www.acmicpc.net/problem/1463

'''
Top-down 방식을 사용하려고 재귀로 구현했는데 RecursionError가 발생해 미통과.


풀이:

n->1로 만들거나 1->n으로 만들 수 있음.
1->n으로 만드는 bottom-up 방식 (반복문)을 사용해보자.

dp[i]: 1부터 i를 만드는 데 필요한 최소 연산 횟수

점화식:
if i % 3 == 0, dp[i] = min(dp[i], dp[i / 3] + 1)
if i % 2 == 0, dp[i] = min(dp[i], dp[i / 2] + 1)
dp[i] = min(dp[i], dp[i - 1] + 1)
'''


# --- 코드1. 해설에 나온 답안 ---
n = int(input())
dp = [0] * (n + 1)    # [0]은 사용안함

# bottom-up 방식
for i in range(2, n+1):
    dp[i] = dp[i - 1] + 1  # 1을 빼는 연산을 가장 먼저 하는 것을 생각해내기 어려울듯함
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
print(dp[n])


# --- 코드2. 내가 구현한 답안 ---
n = int(input())
INF = 10 ** 6
dp = [INF] * (n + 1)    # [0]은 사용안함
dp[1] = 0

# bottom-up 방식
for i in range(2, n+1):
    if i % 3 == 0:
        dp[i] = dp[i // 3] + 1   # min(dp[i], dp[i // 3] + 1)는 어차피 dp[i // 3] + 1임
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    dp[i] = min(dp[i], dp[i - 1] + 1)
print(dp[n])