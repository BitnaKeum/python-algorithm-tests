# 백준 1920번 수 찾기 문제 (실버4)
# https://www.acmicpc.net/problem/1920

'''
이진 탐색을 활용하는 기본 문제.
이진 탐색을 사용하려면 리스트가 정렬되어 있어야하는 점 꼭 유의하기!!
'''


import sys
sys.setrecursionlimit(10000)

n = int(input())
a = sorted(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))


def binary_search(start, end, target):
    if start > end:
        return 0

    mid = (start + end) // 2
    if a[mid] == target:
        return 1
    elif a[mid] > target:
        return binary_search(start, mid - 1, target)
    else:
        return binary_search(mid + 1, end, target)


for target in targets:
    print(binary_search(0, n - 1, target))