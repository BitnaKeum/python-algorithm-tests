# 백준 2138번 전구와 스위치 문제 (골드5)
# https://www.acmicpc.net/problem/2138

'''
미통과. 핵심을 간파하지 못해서 복잡하게 접근했다.
참고: https://velog.io/@cjkangme/%EB%B0%B1%EC%A4%80-2138.-%EC%A0%84%EA%B5%AC%EC%99%80-%EC%8A%A4%EC%9C%84%EC%B9%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC

핵심:
- 순차적으로 순회할 때, i-1번째 값은 현재 인덱스가 i일때 마지막으로 바뀔 수 있음
- i==0일 때는 눌러야하는 명확한 기준이 없으므로, 누르는 경우와 안누르는 경우를 모두 구해서 비교해야 함
'''


def push_switch(S, i):
    # i-1, i, i+1번째 전구 중 범위 이내인 것을 inverse
    for j in range(i-1, i+2):
        if 0 <= j < N:
            S[j] = S[j] ^ 1
    return S


N = int(input())
S = list(map(int, list(input())))
T = list(map(int, list(input())))
INF = 10**6

# 0번째 스위치를 안누르는 경우
S_copy = S[::]
cnt1 = 0
for i in range(1, N):
    if S_copy[i-1] != T[i-1]:
        S_copy = push_switch(S_copy, i)
        cnt1 += 1
if S_copy != T:
    cnt1 = INF

# 0번째 스위치를 누르는 경우
S_copy = S[::]
S_copy = push_switch(S_copy, 0)
cnt2 = 1
for i in range(1, N):
    if S_copy[i-1] != T[i-1]:
        S_copy = push_switch(S_copy, i)
        cnt2 += 1
if S_copy != T:
    cnt2 = INF

answer = min(cnt1, cnt2)
if answer != INF:
    print(answer)
else:
    print(-1)