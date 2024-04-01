# 백준 13398번 연속 합 2 문제 (골드5)
#

'''
미통과. Dynamic Programming 활용 문제인데 풀이 떠올리기가 너무 어려웠다.

풀이:
- 하나의 수를 제거할 수 있음 => 왼쪽부터의 최대 합을 저장하는 배열을 구하고 오른쪽부터의 최대 합을 저장하는 배열을 구함.
  이때의 점화식:
    L[i] = max(L[i-1] + A[i], A[i])
    R[i] = max(R[i+1] + A[i], A[i])
  주어진 예제에 따라 L, R 배열을 구하면,
    L: [10,  6,  9, 10, 15, 21, -14, 12, 33, 32]
    R: [21, 11, 15, 12, 11,  6,  -2, 33, 21, -1]
- 수를 제거 안해도 되기 때문에, 제거하기에 앞서 최대 합을 계산해놓기
- i번째 수를 제거했을 때의 최대 합 점화식: L[i-1] + R[i+1] (단 i가 0일때와 n-1일때는 예외)
'''


# --- 최적의 코드 ---

import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

# L 배열: 왼쪽부터의 최대 합
# R 배열: 오른쪽부터의 최대 합
L = [0] * n
R = [0] * n
L[0] = A[0]
R[n - 1] = A[n - 1]

# 점화식
#   L[i] = max(L[i-1] + A[i], A[i])
#   R[i] = max(R[i+1] + A[i], A[i])
max_num = L[0]
for i in range(1, n):  # 1 ~ (n-1)
    L[i] = max(L[i - 1] + A[i], A[i])
    if L[i] > max_num:  # 수를 제거 안했을 때의 최대 합 구하기
        max_num = L[i]
for i in range(n - 2, -1, -1):  # (n-2) ~ 0
    R[i] = max(R[i + 1] + A[i], A[i])

# i번째 수를 제거했을 때의 최대 합 구하기
# 점화식
#   i==0일 때, R[i+1]
#   i==n-1일 때, L[i-1]
#   1<=i<=n-2일 때, L[i-1] + R[i+1]
if n > 1:
    for i in range(n):
        if i == 0:
            cur_num = R[i + 1]
        elif i == n - 1:
            cur_num = L[i - 1]
        else:
            cur_num = L[i - 1] + R[i + 1]

        if cur_num > max_num:
            max_num = cur_num
print(max_num)