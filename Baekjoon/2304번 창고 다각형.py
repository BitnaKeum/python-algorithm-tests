# 백준 2304번 창고 다각형 문제 (실버2)
# https://www.acmicpc.net/problem/2304

'''
처음 풀어봤다면 어려웠을테지만, 백준 14719번 빗물 문제를 먼저 풀어봐서 쉽게 풀 수 있었다.

풀이:

물이 고이지 않아야함 => 현재 위치를 기준으로, 모든 왼쪽과 오른쪽에 현재 위치의 높이보다 더 높은게 있으면 안됨

- 왼쪽 최대 높이 l_max, 오른쪽 최대 높이 r_max 구하기
- 현재 위치에서 지붕 높이 roof = min(l_max, r_max)
   - 단, if 현재 위치의 높이 > roof이면, roof = 현재 위치의 높이
'''


N = int(input())
grid = [0] * 1002   # line 17에서 i==1000일때 에러 방지를 위해 index 1001까지 만듦
for _ in range(N):
    x, y = map(int, input().split())
    grid[x] = y
answer = 0

l_max = 0
for i in range(1, 1001):
    r_max = max(grid[i+1:])
    roof = min(l_max, r_max)
    if grid[i] > roof:
        roof = grid[i]
    answer += roof
    l_max = max(l_max, grid[i])
print(answer)