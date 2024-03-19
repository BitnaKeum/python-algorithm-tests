# 백준 실버4 1940번 주몽 문제
# https://www.acmicpc.net/problem/1940

'''
n의 최대 범위가 15,000이므로 O(nlogn) 사용가능 => 주어진 값들을 정렬한 후, 투 포인터 활용
'''

n = int(input())
m = int(input())
numbers = sorted(map(int, input().split()))

start, end = 0, n-1
answer = 0
while start < end:
    if numbers[start] + numbers[end] > m:
        end -= 1
    elif numbers[start] + numbers[end] == m:
        answer += 1
        end -= 1
        start += 1
    else:
        start += 1
print(answer)