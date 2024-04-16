# 백준 20006번 랭킹전 대기열 문제 (실버1)
#

'''
시간복잡도가 널널해서 효율적으로 구현하려 애쓰지 않고 편하게 구현했다.
실버1보다 난이도가 쉬운 것 같다.

입장 가능한 방이 없으면 => 새로운 방 생성하고 입장시키기
매칭 조건: 처음 입장한 플레이어의 레벨 기준으로 -10 ~ +10 까지 입장 가능
입장 가능한 방이 여러개이면 => 가장 먼저 생성된 방에 입장
풀방이 되면 게임 시작
'''

import sys
input = sys.stdin.readline

p, m = map(int, input().split()) # p: 플레이어 수, m: 방의 정원
rooms = []
for _ in range(p):
    s = input().split()
    level, nickname = int(s[0]), s[1]
    done = False
    for i, room in enumerate(rooms):
        if len(room) < m and abs(room[0][0] - level) <= 10:    # 입장 가능
            rooms[i].append((level, nickname))
            done = True
            break
    if not done:
        rooms.append([(level, nickname)])    # 새로운 방 생성
for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
    for level, nickname in sorted(room, key=lambda x: x[1]):
        print(level, nickname)