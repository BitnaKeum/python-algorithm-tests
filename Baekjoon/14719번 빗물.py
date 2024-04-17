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


# --- 정답 답안 ---
H, W = map(int, input().split())
blocks = list(map(int, input().split()))
answer = 0

m_left = blocks[0]
for i in range(1, W - 1):
    m_right = max(blocks[i + 1:])

    m = min(m_left, m_right)
    if m - blocks[i] > 0:
        answer += (m - blocks[i])

    m_left = max(m_left, blocks[i])
print(answer)



# --- 내가 작성한 틀린 답안 ---
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