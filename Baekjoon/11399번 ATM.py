# 백준 11399번 ATM 문제 (실버4)
# https://www.acmicpc.net/problem/11399

'''
예제1에서 p: [3,1,4,3,2]
줄을 1-2-3-4-5로 서면 -> 3 + (3+1) + (3+1+4) + (3+1+4+3) + (3+1+4+3+2) = 총 39
줄을 2-5-1-4-3로 서면 -> 1 + (1+2) + (1+2+3) + (1+2+3+3) + (1+2+3+3+4) = 총 32
즉, 총합의 최솟값을 구하려면 p를 오름차순으로 정렬해야함을 알 수 있다!

n의 크기가 1000이고 시간제한 1초이므로 O(n^2) 시간복잡도를 갖는 정렬 알고리즘 사용 가능
-> 삽입 정렬을 사용해서 구현함
'''

n = int(input())
p = list(map(int, input().split()))

# p를 오름차순 정렬 (삽입 정렬)
for i in range(1, n):
    for j in range(i, 0, -1):
        if p[j-1] > p[j]:    # swap
            p[j-1], p[j] = p[j], p[j-1]
        else:
            break
answer = 0
for i in range(n):
    answer += p[i] * (n-i)
print(answer)