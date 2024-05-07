# 백준 19637번 IF문 좀 대신 써줘 문제 (실버3)
# https://www.acmicpc.net/problem/19637

'''
미통과.
binary search는 잘 떠올렸는데, 구현 과정에서 조건 설정을 실수했다.
정확히 딱 들어맞는 구간을 찾으려고 했는데, 그게 아니라 부분 조건을 만족할때마다 값을 저장하고 그 구간을 좁혀가면서 답을 찾아야했다.
'''


# --- 올바른 답안 ---
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
labels = []
for _ in range(N):
    s = input().split()
    labels.append((s[0], int(s[1])))
labels.sort(key=lambda x: x[1])

for _ in range(M):
    power = int(input())

    # Binary Search
    start, end = 0, N - 1
    while start <= end:
        mid = (start + end) // 2
        if labels[mid][1] >= power:
            end = mid - 1
            result = mid
        else:
            start = mid + 1
    print(labels[result][0])


# --- 미통과한 답안 ---
# import sys
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# labels = {}
# for _ in range(N):
#     s = input().split()
#     if int(s[1]) not in labels:
#         labels[int(s[1])] = s[0]
# max_powers = [-1] + sorted(labels.keys())
#
# for _ in range(M):
#     power = int(input())
#
#     start, end = 0, N
#     while start <= end:
#         mid = (start + end) // 2
#         if max_powers[mid - 1] < power <= max_powers[mid]: # 이 조건을 잘못 설정함
#             print(labels[max_powers[mid]])
#             break
#         elif power > max_powers[mid]:
#             start = mid + 1
#         elif power <= max_powers[mid - 1]:
#             end = mid - 1