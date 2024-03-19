# 백준 1929번 소수 구하기 문제 (실버3)
# https://www.acmicpc.net/problem/1929

'''
m,n의 범위가 100만까지 가능하므로, 완전한 이중 반복문으로 구현하면 시간초과가 뜰 것.
=> 배수들을 모두 제거하는 에라토스테네스의 체 방법을 활용. 이는 이중 반복문으로 구현하지만 사실상 시간복잡도는 O(nlog(logn))
'''


# --- 답안: 에라토스테네스의 체를 활용한 최적의 답안 ---
m, n = map(int, input().split())

primes = [True] * (n + 1)
if m == 1:  # 1은 False 처리
    primes[1] = False
for i in range(2, int(n ** 0.5) + 1):  # 2 ~ √n
    if primes[i] == False: # 더 작은 단위의 배수들이 이미 False 처리되었으므로 스킵
        continue
    for idx in range(i + i, n + 1, i):  # i의 배수들을 모두 False 처리 (i 자신은 X)
        primes[idx] = False

for idx in range(m, n + 1):
    if primes[idx]:
        print(idx)