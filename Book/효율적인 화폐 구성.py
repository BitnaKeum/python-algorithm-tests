# 책 이것이 코딩테스트다 p.226 효율적인 화폐 구성 문제
# Dynamic Programming 이용

"""
이런 문제만 보면 모든 경우의 수를 탐색하기 위해 재귀로 접근하는 습관이 있는데, 대부분의 경우 재귀보다 효율적인 답안이 존재했음.
반복문을 사용하여 Bottom-up 방식으로 접근하는 습관을 들이자.

이 문제에서는 각 화폐 단위를 번갈아가며 탐색할 필요 없이, 한 화폐 단위로 가능한 금액을 쭉 탐색하고 다음 화폐 단위로 탐색하면 된다.
"""


# --- 답안1. 최적의 답안 ---
# Bottom-up with DP table

n, m = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
  
MAX = 100000
d = [MAX] * (m+1)
d[0] = 0
for coin in coins:
    for i in range(m-coin+1): # 0 ~ m-coin
        if d[i] != MAX:
            d[i+coin] = min(d[i+coin], d[i] + 1)
if d[m] == MAX:
    print(-1)
else:
    print(d[m])


# --- 답안2 ---
# Top-down with memoization

n, m = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)

MAX = 100000
memo = [MAX] * (m+1)

def top_down(number, cnt):
    memo[number] = min(memo[number], cnt)
    if number <= 0 or number < coins[-1] or cnt > memo[0]:
        return
    
    for i in range(n):
        top_down(number - coins[i], memo[number] + 1)
    
top_down(m, 0)
if memo[0] == MAX:
    print(-1)
else:
    print(memo[0])


# --- 답안3: only 재귀 사용으로 비효율적인 코드 ---
# Top-down

n, m = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)

answer = -1

def top_down(number, cnt):
    global answer
    
    if number == 0:
        if answer == -1 or cnt < answer:
            answer = cnt
        return
    elif number < coins[-1]: # 가장 작은 화폐 단위보다 number 값이 작을 경우
        return
    
    for i in range(n):
        top_down(number - coins[i], cnt + 1)
    
top_down(m, 0)
print(answer)
