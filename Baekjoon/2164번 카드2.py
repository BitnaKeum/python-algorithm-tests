# 백준 2164번 카드2 문제
# https://www.acmicpc.net/problem/2164

'''
Queue 활용 문제.
리스트(스택)을 사용하면 시간 초과 에러가 발생함. pop() 연산이 빈번한 경우에는 효율적인 deque를 사용하자.
'''

from collections import deque

n = int(input())
cards = deque(list(range(1, n+1)))
while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())
print(cards[0])