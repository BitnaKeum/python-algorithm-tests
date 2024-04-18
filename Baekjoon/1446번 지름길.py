# 백준 1446번 지름길 문제 (실버1)
# https://www.acmicpc.net/problem/1446


# --- 답안1. 최적의 답안 ---
'''
모든 인덱스를 앞에서부터 순회하면서, 현재 인덱스의 값과 (직전 인덱스의 값 + 1) 을 비교해 업데이트
현재 위치에서 시작하는 지름길이 있으면 도착 위치에서의 거리를 비교해 업데이트
'''
N, D = map(int, input().split())
shortcut = []
for _ in range(N):
    s, e, d = map(int, input().split())
    if e > D or e - s < d:
        continue
    shortcut.append((s, e, d))
dist = list(range(D + 1))

for i in range(D + 1):
    dist[i] = min(dist[i], dist[i - 1] + 1)
    for s, e, d in shortcut:  # N<=12이므로 매번 순회해도 ok
        if s == i:
            dist[e] = min(dist[e], dist[s] + d)
print(dist[D])


# --- 답안2. 내가 작성한 답안 ---
'''
코드는 간결하지만 아이디어 떠올리기가 꽤 복잡했다.
3번째 test case에서 (80 190 100)이 골칫거리였다.
지름길 (80 190 100)을 선택하는 것보다 지름길 (140 160 14), (160 180 14)를 선택해 190에 도착하는 것이 더 거리가 짧다.
처음에는 시작 위치가 작은 순서대로 queue에 저장했었는데,
이렇게 하면 지름길 (80 190 100)과 같이 시작 위치는 더 작지만 이후의 지름길보다 도착 위치가 더 큰 지름길이 최단거리가 아닌 경우를 올바르게 처리하지 못하게 된다.

예를 들어,
지름길 (80 190 100) 처리:
위치:  80      140       160       180       190
거리: d[80]   d[140]   d[160]    d[180]   d[80]+100  =  74   d[140]   d[160]   d[180]   74+100
->
지름길 (140 160 14) 처리:
위치:  80      140       160        180      190
거리: d[80]  d[140]   d[140]+14   d[180]  d[80]+100   =   74    134    134+14    d[180]    174
->
지름길 (160 180 14) 처리:
위치:  80      140      160         180         190
거리: d[80]  d[140]   d[140]+14   d[160]+14   d[80]+100   =   74    134    148    162    174
=> 190에 도착하기 위한 거리를 계산해보면, 방금 구한 d[180]에 10을 더한 값 (=162+10=172)이 이미 구해놓은 d[80]+100 (=174)보다 작으므로 예외 발생.

따라서, 도착 위치가 작은 순서대로 queue에 저장해야한다.
지름길 (140 160 14), (160 180 14)을 먼저 처리한 후 (80 190 100)를 만나면, 이전 지름길에서 구한 거리가 더 짧기 때문에 이 지름길은 선택되지 않는다.

현재 위치에서 시작하는 지름길이 선택되었다면, 단축된 거리만큼 이후의 모든 거리 값으로부터 빼준다.
'''
from queue import PriorityQueue

N, D = map(int, input().split())
dist = list(range(D + 1))
q = PriorityQueue()

for _ in range(N):
    s, e, d = map(int, input().split())
    if e > D or e - s < d:
        continue
    q.put((e, s, d))  # 도착위치가 작은 순으로 저장

while q.qsize() > 0:
    e, s, d = q.get()

    diff = dist[e] - (dist[s] + d)
    dist[e] = min(dist[e], dist[s] + d)
    if dist[e] == (dist[s] + d):
        for i in range(e + 1, D + 1):
            dist[i] -= diff
print(dist[D])