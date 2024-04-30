# 백준 17615번 볼 모으기 문제 (실버1)
# https://www.acmicpc.net/problem/17615

'''
미통과.
뭔가 감이 오긴 했는데 가능한 4가지 경우를 모두 수행할 생각을 못하고 규칙을 찾으려다 실패했다.
가능한 경우를 모두 수행하는 방안에 익숙해지도록 연습해야겠다.

풀이:

가능한 경우
1. 왼쪽 R, 오른쪽 B
  1-1. R을 옮기기
  1-2. B를 옮기기
2. 왼쪽 B, 오른쪽 R
  2-1. R을 옮기기
  2-2. B를 옮기기
위의 4가지 경우를 모두 해보고 최소값을 반환하면 된다!

예제1:

경우 2-1을 수행할 때,
RBBBRBRRR에서 [0]과 [4] 위치의 R을 오른쪽으로 옮겨야함
만약 [0]을 먼저 옮기면 BBBRRBRRR -> BBBRBRRRR -> BBBBRRRRR, 총 3번 옮겨야함
만약 [4]를 먼저 옮기면 RBBBBRRRR -> BBBBRRRRR, 총 2번 옮겨야함
=> 이를 통해, 오른쪽으로 옮겨야하는 상황에서는 더 오른쪽에 있는 것부터 진행해야함을 알 수 있음
=> 또한, 총 옮겨야하는 횟수는 가장 오른쪽에 연속된 R 문자열을 제외했을 때 존재하는 R 문자의 갯수와 동일함을 알 수 있음
'''

N = int(input())
balls = input()
counts = []

# R 또는 B로만 이루어진 경우
if balls.count('B') == 0 or balls.count('R') == 0:
    print(0)
else:
    # 경우 1-1: 왼쪽 R, 오른쪽 B (R을 왼쪽으로 옮기기)
    if balls[0] == 'R':
        idx = balls.find('B')
        counts.append(balls[idx:].count('R'))
    # 경우 1-2: 왼쪽 R, 오른쪽 B (B를 오른쪽으로 옮기기)
    if balls[-1] == 'B':
        idx = balls.rfind('R')
        counts.append(balls[:idx+1].count('B'))
    # 경우 2-1: 왼쪽 B, 오른쪽 R (R을 오른쪽으로 옮기기)
    if balls[-1] == 'R':
        idx = balls.rfind('B')
        counts.append(balls[:idx+1].count('R'))
    # 경우 2-2: 왼쪽 B, 오른쪽 R (B를 왼쪽으로 옮기기)
    if balls[0] == 'B':
        idx = balls.find('R')
        counts.append(balls[idx:].count('B'))
    print(min(counts))