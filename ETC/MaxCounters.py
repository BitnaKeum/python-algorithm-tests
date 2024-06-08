# Codility lesson4 MaxCounters 문제 (Medium)
# https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/start/

'''
미통과. 시간 초과 케이스를 해결하지 못함.

원소가 N개인 counter는 처음에 모두 0으로 초기화
A[K] 값 (=X)이   1~N 사이면  => increase
                N+1 이상이면 => max counter
O(NlogN)까지 가능

풀이:

A[0]: (0, 0, 1, 0, 0)
A[1]: (0, 0, 1, 1, 0)
A[2]: (0, 0, 1, 2, 0)
A[3]: max_counter = 2
A[4]: (3, 0, 1, 2, 0)
A[5]: (3, 0, 1, 3, 0)
A[6]: (3, 0, 1, 4, 0)
마지막 for문: (3, 2, 2, 4, 2)

만약 A[7]=6, A[8]=1가 있었다면, A[6]에 이어서
A[7]: max_counter = 4
A[8]: (5, 0, 1, 4, 0)
마지막 for문: (5, 4, 4, 4, 4)
'''


# --- 최적의 코드 ---
# 시간복잡도: O(N+M)
def solution(N, A):
    counter = [0] * (N + 1) # [0]는 사용 X
    max_num = max_counter = 0
    for X in A:
        if 1 <= X <= N:
            if counter[X] < max_counter:
                counter[X] = max_counter + 1
            else:
                counter[X] += 1
            max_num = max(max_num, counter[X])
        else:
            max_counter = max_num
    for idx in range(1, N+1):
        if counter[idx] < max_counter:
            counter[idx] = max_counter

    return counter[1:]


# 77%로 틀린 코드
# 시간복잡도: O(N^2)
# def solution(N, A):
#     counter = [0] * (N + 1) # [0]는 사용 X
#     max_num = 0
#     for X in A:
#         if 1 <= X <= N:
#             counter[X] += 1
#             max_num = max(max_num, counter[X])
#         else:
#             counter = [max_num] * (N + 1) # 이 코드 때문에 시간 초과 발생
#     return counter[1:]