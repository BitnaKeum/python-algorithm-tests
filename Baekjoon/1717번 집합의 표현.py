# 백준 1717번 집합의 표현 (골드5)
# https://www.acmicpc.net/problem/1717

'''
유니온 파인드 활용 문제.
union 연산에서 a와 b를 연결시키는 실수를 했음. 유의하기.
'''


import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int, input().split())
parents = list(range(n + 1))


def union(a, b):
    parent_a = find(a)
    parent_b = find(b)
    if parent_a <= parent_b:
        parents[parent_b] = parent_a
    else:
        parents[parent_a] = parent_b

def find(a):
    if a == parents[a]:  # 대표노드
        return a
    else:
        parent_a = find(parents[a])
        parents[a] = parent_a  # 대표노드 업데이트
        return parent_a


for _ in range(m):
    op_num, a, b = map(int, input().split())
    if op_num == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')