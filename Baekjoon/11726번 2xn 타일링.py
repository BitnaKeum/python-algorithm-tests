# 백준 11726번 2xn 타일링 문제 (실버3)
# https://www.acmicpc.net/problem/11726


'''
n번째를 채우는 방법의 수: (n-1)번째 + (n-2)번째
D(n) = D(n-1) + D(n-2)
D(1) = 1
D(2) = 2
D(3) = D(2) + D(1) = 3
...
'''


# --- 답안1. 최적의 답안 (DP 활용) ---
n = int(input())
dp_table = [0] * (n+1)
dp_table[1] = 1
if n != 1:  # 조건문을 안 달아주면 n == 1일때 IndexError 발생
    dp_table[2] = 2
    for i in range(3, n+1):
        dp_table[i] = (dp_table[i-1] + dp_table[i-2]) % 10007   # 10007로 나눈 나머지를 저장하지 않으면 오버플로우 발생
print(dp_table[n])


# --- 답안2. 시간 초과 답안 (재귀 활용) ---
import sys
sys.setrecursionlimit(10000)

n = int(input())
answer = 0

def recursion(sum):
    global answer
    if sum == n:
        answer += 1
        return
    elif sum > n:
        return
    recursion(sum + 2)
    recursion(sum + 1)

recursion(0)
print(answer % 10007)