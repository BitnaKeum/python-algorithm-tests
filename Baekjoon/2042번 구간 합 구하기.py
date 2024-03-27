# 백준 2042번 구간 합 구하기 문제 (골드1)
# https://www.acmicpc.net/problem/2042


'''
세그먼트 트리 (구간 합) 활용 문제.
'''


import sys
input = sys.stdin.readline


def get_segtree_idx(query_idx):
    return query_idx + (2 ** k - 1)


def range_sum(start_idx, end_idx):
    answer = 0
    while start_idx <= end_idx:
        if start_idx % 2 == 1:
            answer += tree[start_idx]
            start_idx += 1
        if end_idx % 2 == 0:
            answer += tree[end_idx]
            end_idx -= 1
        start_idx = start_idx // 2
        end_idx = end_idx // 2
    return answer


def update(idx, new_value):
    diff = new_value - tree[idx]
    while idx != 1:
        tree[idx] += diff
        idx = idx // 2


n, cnt1, cnt2 = map(int, input().split())

# 2^k >= N 인 최소 k 찾기
length = n
k = 0
while length != 0:
    length = length // 2
    k += 1

# 구간 합 세그먼트 트리 만들기
# 2^(k+1) 크기의 리스트 만들기
tree_size = 2 ** (k + 1)
tree = [0] * (tree_size + 1)
for i in range(2 ** k, 2 ** k + n):
    tree[i] = int(input())
# 부모 노드로 올라가면서 값 채우기
for i in range(tree_size, 1, -1):
    tree[i // 2] += tree[i]

# 질의에 따라 연산 수행하기
for _ in range(cnt1 + cnt2):
    a, b, c = map(int, input().split())
    if a == 1:  # 데이터 업데이트
        b = get_segtree_idx(b)
        update(b, c)
    else:  # b번째~c번째 수의 구간 합
        b, c = get_segtree_idx(b), get_segtree_idx(c)
        print(range_sum(b, c))