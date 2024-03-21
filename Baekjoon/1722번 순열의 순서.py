# 백준 1722번 순열의 순서 문제 (골드5)
# https://www.acmicpc.net/problem/1722

'''
순열 활용 문제.
이전 자리에서 가능한 경우의 수를 활용해서 풀어야 하는데, 이 부분이 익숙하지 않아 어려웠다.
개념은 얼추 이해했으나 소문제2를 구현 못해서 미통과.

문제 이해하는 데에 도움된 블로그 -> https://kosaf04pyh.tistory.com/211
코드 구현하는 데에 도움된 블로그 -> https://dreamtreeits.tistory.com/211
'''


import math

N = int(input())
input_list = list(map(int, input().split()))

'''
N이 4인 경우,
가능한 순열은 1234, 1243, 1324, 1342, 1423, 1432, 2134, 2143, ...
자리별 경우의수: 첫째자리 4!, 둘째자리 3!,     셋째자리 2!,     넷째자리 1!
자리별 경우의수: 첫째자리 N!, 둘째자리 (N-1)!, 셋째자리 (N-2)!, 넷째자리 (N-3)!
'''

numbers = list(range(1, N + 1))

# 소문제1: k번째 수열 출력하기
if input_list[0] == 1:
    k = input_list[1]  # 3
    answer = []
    for i in range(1, N + 1):  # i번째 자리
        prev_cases = math.factorial(N - i)
        div_k = (k - 1) // prev_cases
        # k=8, !=6 -> [1]
        # k=7, !=6 -> [1]
        # k=6, !=6 -> [0]
        # (k-1) // !
        answer.append(numbers[div_k])
        numbers.remove(numbers[div_k])
        k -= div_k * prev_cases
    print(*answer)

# 소문제2: perm이 몇번째 수열인지 출력하기
else:
    perm = input_list[1:]  # [1,3,2,4]
    sorted_perm = sorted(perm)  # [1,2,3,4]
    answer = 1
    for i in range(1, N + 1):
        prev_cases = math.factorial(N - i)
        cur_num = perm[i - 1]
        cur_num_idx = sorted_perm.index(cur_num)
        sorted_perm.remove(cur_num)
        answer += cur_num_idx * prev_cases
    print(answer)