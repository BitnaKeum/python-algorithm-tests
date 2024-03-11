# 백준 11286번 절댓값 힙 문제 (실버1)
# https://www.acmicpc.net/problem/11286

'''
우선순위 큐 (Priority Queue) 활용 문제.
우선순위 큐를 제대로 익히지 않아 구현하기가 너무 어려웠는데, 개념을 잘 익혔다면 쉽게 풀었을 것 같다.
'''

from queue import PriorityQueue
import sys
input = sys.stdin.readline
print = sys.stdout.write

queue = PriorityQueue()

n = int(input())
for _ in range(n):
    num = int(input())
    if num != 0:
        queue.put((abs(num), num))
    else:
        if queue.empty():
            print('0\n')
        else:
            print(str(queue.get()[1]) + '\n')