# 백준 14501번 퇴사 문제 (실버3)
# https://www.acmicpc.net/problem/14501

'''
Dynamic Programming 활용 문제. 미통과.


생각의 과정:

1일->4일->5일
10 + 20 + 15 = 45

2일
20

3일->4일->5일
10 + 20 + 15 = 45

주의: 해당 날짜를 스킵하는게 나을수도 있음

D[i]: i일~n일까지 최대 금액? or 1일~i일까지 최대 금액?

점화식:
D[i + T[i]] += P[i] -> 뭔가 이상


앞에서부터 하니까 이상한데... 뒤에서부터로 생각해볼까?
주의: 해당 날짜를 스킵하는게 나을수도 있음

7일
x

6일
x

5일
15

4일->5일
20 + 15

3일->4일->5일
10 + 20 + 15

2일
20 -> 범위 안이라고 무조건 선택하지 말고, 이걸 선택하면 손해니까 안하게 할 방법을 생각해보자
max(i를 선택했을때, i를 선택안했을때)
max(i를 선택했을때, D[i+1])
그러면 D[i]: i일~n일까지의 최대 금액

D = [0, 10+D[4], 10+20+15, 10+20+15, 20+15, 15, 0, 0]
D = [0, P[1]+D[4], D[3], P[3]+D[4], P[4]+D[5], P[5]+D[7], 0, 0]
max(P[i]+D[i+T[i]], D[i+1]) # max(i를 선택했을때, i를 선택안했을때)

i를 선택하지 않는 경우 -> 기간이 초과 or 선택안했을때보다 금액이 작은 경우
D[i]가 i일~n일까지의 금액이므로 i를 선택하지 않는 경우 (i+1)일~n일까지의 금액이고, 이는 즉 D[i+1]

기간 초과인 경우
n=10이고 T[10]=1일때를 생각해보면, 마지막날에 1일 걸리는 상담은 가능함
=> i+T[i] > n+1 이면 기간 초과

정리
- if i+T[i] > n+1 (기간 초과), D[i] = D[i+1]
- else, D[i] = max(P[i]+D[i+T[i]], D[i+1])
- 최종적으로 return D[1]
'''


# --- 답안1. 최적의 코드 (해설 참조) ---
# 뒤에서 앞으로 접근하기
n = int(input())
T = [0] * (n + 1)  # 기간
P = [0] * (n + 1)  # 금액
for i in range(1, n + 1):
    T[i], P[i] = map(int, input().split())
# T: [0, 3, 5, 1, 1, 2, 4, 2]
# P: [10, 20, 10, 20, 15, 40, 200]
D = [0] * (n + 2)  # i==n일때, D[i+1]의 값이 필요하므로 (n+2) 사이즈로 만듦

for i in range(n, 0, -1):  # n ~ 1
    if i + T[i] > n + 1:  # i를 선택했을때 기간 초과
        D[i] = D[i + 1]
    else:
        D[i] = max(P[i] + D[i + T[i]], D[i + 1])
print(D[1])


# --- 답안2. 앞에서 뒤로 접근하도록 시도 (실패) ---
'''
D[i]: 1일부터 i일까지의 최대 금액

if i+T[i] > n+1, continue
else, D[i+T[i]] = max(D[i+T[i]], D[i]+P[i])
'''

n = int(input())
T = [0] * (n+1) # 기간
P = [0] * (n+1) # 금액
for i in range(1, n+1):
    T[i], P[i] = map(int, input().split())
D = [0] * (n+2)

for i in range(1, n+1): # 1 ~ n
    if i+T[i] > n+1:
        continue
    else:
        D[i+T[i]] = max(D[i+T[i]], D[i]+P[i])
print(max(D))

'''
예제1:
T = [0, 3, 5, 1, 1, 2, 4, 2]
P = [10, 20, 10, 20, 15, 40, 200]
D[4] = 10
D[7] = 20
D[4] = 10
D[5] = 10 + 20 (D[i]+P[i])
D[7] = max(D[7], D[5]+P[5]) = max(20, 30+15) = 45 -> 정답

예제2:
T = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
P = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
D[2] = 1
D[3] = max(D[3], D[2]+P[2]) = D[2]+P[2] = 3
D[4] = max(D[4], D[3]+P[3]) = D[3]+P[3] = 6
...
D[11] = max(D[11], D[10]+P[10]) = D[10]+P[10] = 55 -> 정답

예제3:
T = [0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
P = [0, 10, 9, 8, 7, 6, 10, 9, 8, 7, 6]
D[6] = D[1]+P[1] = 10
D[7] = D[2]+P[2] = 9
D[8] = D[3]+P[3] = 8
D[9] = D[4]+P[4] = 7
D[10] = D[5]+P[5] = 6
D[11] = D[6]+P[6] = 10+10 = 20 -> 정답

예제4:
T = [0, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5]
P = [0, 50, 40, 30, 20, 10, 10, 20, 30, 40, 50]
D[6] = 50
D[6] = 50
D[6] = 50
D[6] = 50
D[6] = 50
D[7] = 60
D[9] = D[7]+P[7] = 60+20 = 80
D[11] = D[8]+P[8] = 30 -> 오답 !

이 코드에서는 i를 선택하지 않을때 이전의 최대값이 보존되지 않아서 틀림
앞에서부터 구현하는건 안되는듯 싶다.
'''