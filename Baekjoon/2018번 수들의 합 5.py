# 백준 실버5 2018번 수들의 합 5 문제
# https://www.acmicpc.net/problem/2018

'''
투 포인터를 사용하는 기본적인 문제.
배열을 따로 만들면 메모리 초과 에러가 뜨게 된다. 배열을 만들지 않고도 해결할 수 있음을 익히기!
'''

n = int(input())

start, end = 1, 1
sum = 1
cnt = 1
while end < n:
    if sum < n:
        end += 1
        sum += end
    elif sum == n:
        end += 1
        sum += end
        cnt += 1
    else:
        sum -= start
        start += 1
print(cnt)