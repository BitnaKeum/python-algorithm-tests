# 백준 1406번 에디터 문제 (실버2)
# https://www.acmicpc.net/problem/1406

'''
문자열 슬라이싱을 사용해 원래 문자열과 동일한 길이의 문자열을 할당하는 연산은 시간복잡도가 O(n).
시간 초과를 피하기 위해 deque를 사용해야 함.
'''

# --- 답안1. deque를 사용해 통과한 코드 ---
from collections import deque
import sys
input = sys.stdin.readline

seq = list(input().rstrip())
queue_left, queue_right = deque(seq), deque()
M = int(input())
for _ in range(M):
    cmd = input().rstrip()

    if cmd == "L":  # 왼쪽으로 한칸 옮기기
        if queue_left:
            queue_right.appendleft(queue_left.pop())
    elif cmd == "D":  # 오른쪽으로 한칸 옮기기
        if queue_right:
            queue_left.append(queue_right.popleft())
    elif cmd == "B":  # 왼쪽 문자 하나 삭제
        if queue_left:
            queue_left.pop()
    else:  # insert_ch 문자를 왼쪽에 추가
        cmd, insert_ch = cmd.split()
        queue_left.append(insert_ch)
print(''.join(list(queue_left) + list(queue_right)))


# --- 답안2. 문자열 슬라이싱 사용 (시간 초과) ---
# 반복문 내에 O(n) 연산을 사용해서 시간 초과 발생
# import sys
# input = sys.stdin.readline.rstrip
#
# seq = input()
# M = int(input())
# cursor = len(seq)  # 문자열 맨 뒤에 위치
# for _ in range(M):
#     cmd = input()
#
#     if cmd == "L":  # 왼쪽으로 한칸 옮기기
#         cursor = max(cursor - 1, 0)
#     elif cmd == "D":  # 오른쪽으로 한칸 옮기기
#         cursor = min(cursor + 1, len(seq))
#     elif cmd == "B":  # 왼쪽 문자 하나 삭제
#         if cursor > 0:
#             seq = seq[:cursor - 1] + seq[cursor:]
#             cursor -= 1
#     else:  # insert_ch 문자를 왼쪽에 추가
#         cmd, insert_ch = cmd.split()
#         seq = seq[:cursor] + insert_ch + seq[cursor:]
#         cursor += 1
# print(seq)


# --- 답안3. 리스트 연산 사용 (시간 초과) ---
# 반복문 내에 O(n) 연산을 사용해서 시간 초과 발생
# import sys
# input = sys.stdin.readline
#
# seq = list(input().rstrip())
# seq_len = len(seq)
# cursor = seq_len  # 문자열 맨 뒤에 위치
# M = int(input())
# for _ in range(M):
#     cmd = input().rstrip()
#
#     if cmd == "L":  # 왼쪽으로 한칸 옮기기
#         cursor = max(cursor - 1, 0)
#     elif cmd == "D":  # 오른쪽으로 한칸 옮기기
#         cursor = min(cursor + 1, seq_len)
#     elif cmd == "B":  # 왼쪽 문자 하나 삭제
#         if cursor == seq_len:
#             seq.pop()   # O(1)
#         elif cursor > 0:
#             del seq[cursor - 1] # O(n)
#         cursor -= 1
#         seq_len -= 1
#     else:  # insert_ch 문자를 왼쪽에 추가
#         cmd, insert_ch = cmd.split()
#         if cursor == seq_len:
#             seq.append(insert_ch)   # O(1)
#         else:
#             seq.insert(cursor, insert_ch)   # O(n)
#         cursor += 1
#         seq_len += 1
# print(seq)