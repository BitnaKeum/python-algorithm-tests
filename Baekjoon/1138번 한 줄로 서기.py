# 백준 1138번 한 줄로 서기 문제 (실버2)
# https://www.acmicpc.net/problem/1138

'''
핵심:
자기보다 키가 큰 사람이 왼쪽에 몇 명 있었는지 주어진 수 == line에서 아직 채워지지 않은 자리들에 대한 index

예제1:
_ _ 1 _
_ 2 1 _
_ 2 1 3
4 2 1 3

예제4:
_ _ _ _ _ _ 1
_ 2 _ _ _ _ 1
_ 2 3 _ _ _ 1
_ 2 3 4 _ _ 1
_ 2 3 4 _ 5 1
6 2 3 4 _ 5 1
6 2 3 4 7 5 1
'''


# --- 답안1. 내가 작성한 코드 ---
N = int(input())
taller = [-1] + list(map(int, input().split())) # [0]은 사용 X
line = [0] * N
empty_idxes = list(range(N))

for height in range(1, N+1):
    idx = empty_idxes[taller[height]]
    line[idx] = height
    del empty_idxes[taller[height]]
print(*line)


# --- 답안2. 최적의 코드 (참고) ---
# N = int(input())
# taller = [-1] + list(map(int, input().split())) # [0]은 사용 X
# line = []
#
# for i in range(N, 0, -1):
#     line.insert(taller[i], i)
# print(*line)