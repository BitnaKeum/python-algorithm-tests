# 백준 17298번 오큰수 문제
# https://www.acmicpc.net/problem/17298

'''
이중 반복문으로 구현했으나 n의 크기가 커서 시간 초과로 미통과.
이렇게도 스택을 활용할 수 있다는 것을 더 많이 풀어서 익혀야겠다.
'''


n = int(input())
seq = list(map(int, input().split()))

# --- 답안1. 최적의 답안 ---
# 스택 활용
stack = []
answer = [-1] * n
for i in range(n):
    while stack and seq[stack[-1]] < seq[i]:
        answer[stack.pop()] = seq[i]
    stack.append(i)
for num in answer:
    print(num, end=" ")


# --- 답안2. 비효율적인 답안 ---
# 이중 반복문으로 구현 => 시간 초과
for i in range(n):
    num = seq[i]
    nge = -1
    for j in range(i+1, n):
        if seq[j] > num:
            nge = seq[j]
            break
    print(nge, end=" ")