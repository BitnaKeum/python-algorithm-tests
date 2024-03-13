# 백준 2023번 신기한 소수 문제 (골드5)
# https://www.acmicpc.net/problem/2023

'''
DFS 활용 문제.
핵심은 파악했으나 방문 여부를 기록하지 않아도 된다는 것을 깨닫지 못해서 굉장히 복잡하게 접근했음.
더 다양한 DFS 활용 문제를 접해보는 것이 필요하다.
'''


import sys
sys.setrecursionlimit(10000)

n = int(input())

def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def dfs(num):
    if len(str(num)) < n:
        for i in [1, 3, 7, 9]:
            if is_prime(num * 10 + i):
                dfs(num * 10 + i)
    else:
        print(num)


dfs(2)
dfs(3)
dfs(5)
dfs(7)
