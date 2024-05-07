# 백준 22233번 가희와 키워드 문제 (실버2)
# https://www.acmicpc.net/problem/22233


# --- 답안1. Set 자료형의 difference_update() 함수 사용 (참고) ---
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memo = {input().rstrip() for _ in range(N)}
for _ in range(M):
    keywords = set(input().rstrip().split(','))
    memo.difference_update(keywords)
    print(len(memo))


# --- 답안2. 해시 테이블 활용 ---
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memo = {input().rstrip(): True for _ in range(N)}
for _ in range(M):
    keywords = input().rstrip().split(',')
    for keyword in keywords:
        try:
            del memo[keyword]
        except:
            continue
    print(len(memo))