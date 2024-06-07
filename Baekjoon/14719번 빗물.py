# 백준 14719번 빗물 문제 (골드5)
# https://www.acmicpc.net/problem/14719

'''
미통과.

풀이:

(참고 링크: https://velog.io/@rhdmstj17/백준-14719번-빗물-python-시뮬레이션-골드-5)
맨 왼쪽 칸과 맨 오른쪽 칸을 제외하고 나머지 칸을 순회하면서
현재 칸을 기준으로 왼쪽에서의 최대값 m_left, 오른쪽에서의 최대값 m_right 구하기
빗물이 고이는 높이: m = min(m_left, m_right)
빗물이 고이는 양: m - 현재 칸 높이 -> 만약 결과 값이 음수이면 무시
'''


# --- 최적의 답안 (참고) ---
H, W = map(int, input().split())
blocks = list(map(int, input().split()))
answer = 0

max_left = blocks[0]
for idx in range(1, W - 1):
    # max_left, max_right = max(blocks[:idx]), max(blocks[idx+1:]) # 이렇게 작성해도 되지만 line 22,31을 통해 효율성 높임

    max_right = max(blocks[idx + 1:])
    rain_height = min(max_left, max_right)
    if rain_height - blocks[idx] > 0:
        answer += (rain_height - blocks[idx])

    max_left = max(max_left, blocks[idx])

print(answer)



# --- 나의 오답 코드1 ---
# queue를 이용해서 빗물이 고이는 양 옆의 벽을 찾도록 구현했다.
# 웬만한 테스트케이스는 통과하는것 같은데 조건문도 많고 복잡하게 구현한 것 같아서 버림.
# from collections import deque
#
# H, W = map(int, input().split())
# blocks = list(map(int, input().split()))
# answer = 0
#
# q = deque()
# for i in range(W):
#     if q and q[0] <= blocks[i]:
#         wall = q.popleft()
#         while q:
#             answer += (wall - q.popleft())
#     if i < W-1:
#         q.append(blocks[i])
#     else:
#         if len(q) > 1:
#             wall = min(q.popleft(), blocks[i])
#             while q:
#                 answer += (wall - q.popleft())
# print(answer)


# --- 나의 오답 코드2 ---
# 핵심 풀이법은 떠올렸으나, 각 인덱스마다 반복하는 것이 아니라 해당 구간을 한꺼번에 계산하려고 해서 코드가 스파게티화됐고 결국 틀렸다.
# H, W = map(int, input().split())
# blocks = list(map(int, input().split()))
# answer = 0
#
# idx = 1
# while idx < W:
#     max_left, max_right = max(blocks[:idx + 1]), max(blocks[idx + 1:])
#     rain_height = min(max_left, max_right)
#
#     while idx < W:
#         if blocks[idx] >= rain_height:
#             break
#         answer += (rain_height - blocks[idx])
#         idx += 1
#     # idx: 이전 step의 오른쪽 벽
#
#     while idx < W:
#         if blocks[idx] < rain_height:
#             break
#         idx += 1
#     # idx: 다음 step의 왼쪽 벽+1
#
# print(answer)