# 백준 1863번 스카이라인 쉬운거 문제 (골드4)
# https://www.acmicpc.net/problem/1863


# --- 답안1. 최적의 답안 (절반 참고) ---
# Stack 활용
# 핵심: Stack의 마지막 값보다 현재 값이 더 작으면 건물 개수를 +1시킴. Stack에서 pop()하고 조건 확인을 반복.
# 왜 현재 값이 더 작을때여야할까? -> 현재 값이 0일 때를 생각해보면 이해될것임
import sys
input = sys.stdin.readline

n = int(input())
answer = 0
stack = []
for _ in range(n):
    x, y = map(int, input().split())
    while stack and stack[-1] > y:
        answer += 1
        stack.pop()
    if y == 0 or (stack and stack[-1] == y):
        continue
    stack.append(y)
answer += len(stack)

print(answer)


# --- 답안2. 나의 답안 (구현) ---
# 0인 곳을 기준으로 구간을 분할해서, 구간 내 최솟값을 일괄적으로 빼는 과정을 반복
# x값은 상관이 없음
import sys
input = sys.stdin.readline

n = int(input())
skyline = []
for _ in range(n):
    x, y = map(int, input().split())
    skyline.append(y)
skyline.append(0)

answer = 0
i = 0
while i <= n:
    if skyline[i] == 0:
        i += 1
        continue
    for j in range(i + 1, n + 1):   # i 이후부터 제일 먼저 등장하는 0의 인덱스 찾기
        if skyline[j] == 0:
            zero_idx = j
            break
    min_height = min(skyline[i:zero_idx])
    for j in range(i, zero_idx):
        skyline[j] -= min_height
    answer += 1

print(answer)