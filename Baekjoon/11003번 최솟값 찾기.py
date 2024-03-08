# 백준 11003번 최솟값 찾기 문제 (플래티넘5)
# https://www.acmicpc.net/problem/11003

'''
단순히 슬라이딩 윈도우를 활용해 해결할 수 있을 것 같았으나, 시간 초과 에러를 해결할 수 없었음.
이 문제는 지정된 범위 내에서 최소값을 찾아야하고, 그 범위는 한칸씩 슬라이딩하면서 이전 값이 제거되고 새로운 값이 포함됨.
만약 정렬 알고리즘을 사용할 경우 시간복잡도는 O(nlogn) -> 5,000,000 * 22.xx = 약 1억 1천만번의 연산이 필요.
그러나, 이 문제의 시간 제한은 2.4초 -> 약 9천6백만번의 연산 수용 가능.
따라서 더 효율적인 알고리즘을 사용해야 하므로 deque 자료형을 이용해서 정렬을 구현!
    - deque의 뒤부터 탐색(큰 값부터 탐색)하면서,
    - 새로운 값보다 큰 값들을 모두 제거
    - 새로운 값보다 작은 값을 발견하면 탐색 중단 (그보다 앞에 위치한 값들은 더 작으므로)
    - 이 과정을 반복하면 결과적으로 오름차순 정렬이 됨
다만, 문제에서 지정된 간격 L 내의 값들 중에서 최소값을 찾으라 했으므로, deque에 값을 저장할 때 인덱스도 함께 저장하고, 인덱스로 간격을 체크해서 간격 외의 값을 제거
(문제는 짧지만 플래티넘 레벨답다...)
'''


### 답안1. 최적의 답안 (deque 활용) ###
from collections import deque

N, L = map(int, input().split())
A_list = list(map(int, input().split()))
mydeque = deque()
for i in range(N):
    num = A_list[i]

    # deque에서 현재 값보다 큰 값들을 제거
    while mydeque and mydeque[-1][1] > num:
        mydeque.pop()

    # deque에 현재 값을 삽입
    mydeque.append((i, num))

    # 현재 인덱스로부터 간격 L을 벗어난 인덱스의 값들을 제거
    if i - mydeque[0][0] + 1 > L:
        mydeque.popleft()

    print(mydeque[0][1], end=" ")


### 답안2. 시간 초과 (슬라이딩 윈도우만 활용) ###
# N, L = map(int, input().split())
# A_list = list(map(int, input().split()))
#
# for i in range(N):
#     start = i - L + 1
#     if i == 0:
#         if start < 0:
#             start = 0
#         D_i = min(A_list[start:i + 1])
#     else:
#         if start < 0:
#             D_i = min(D_i, A_list[i])
#         else:
#             if D_i == A_list[start - 1]:
#                 if D_i in A_list[start:i]:
#                     D_i = min(D_i, A_list[i])
#                 else:
#                     D_i = min(A_list[start:i + 1])
#             else:
#                 D_i = min(D_i, A_list[i])
#
#     print(D_i, end=" ")