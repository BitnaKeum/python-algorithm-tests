# 백준 2531번 회전 초밥 문제 (실버1)
# https://www.acmicpc.net/problem/2531


# --- 코드1. 투 포인터 이용 ---
import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())  # 벨트에 놓인 접시 수, 초밥의 종류 수, 연속해서 먹어야하는 수, 쿠폰 번호
belt = [int(input()) for _ in range(N)]

cnt = [0] * (d + 1)  # 초밥 종류별 먹은 갯수
start, end = 0, k - 1
answer = 1
cnt[c] += 1
for s in belt[:k]:
    if cnt[s] == 0:
        answer += 1
    cnt[s] += 1

# 투 포인터 알고리즘
type_cnt = answer
while start < N:
    cnt[belt[start]] -= 1
    if cnt[belt[start]] == 0:
        type_cnt -= 1
    start += 1

    end = (end + 1) % N
    cnt[belt[end]] += 1
    if cnt[belt[end]] == 1:
        type_cnt += 1

    answer = max(answer, type_cnt)
print(answer)


# --- 코드2. queue 이용 ---
from collections import deque
import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())  # 벨트에 놓인 접시 수, 초밥의 종류 수, 연속해서 먹어야하는 수, 쿠폰 번호
belt = [int(input()) for _ in range(N)]

queue = deque(belt[:k])
answer = len(set(list(queue) + [c]))
for i in range(1, N):
    queue.popleft()
    queue.append(belt[(i + k - 1) % N])
    answer = max(answer, len(set(list(queue) + [c])))
print(answer)
