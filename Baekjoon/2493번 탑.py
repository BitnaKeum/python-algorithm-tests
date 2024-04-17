# 백준 2493번 탑 문제 (골드5)
# https://www.acmicpc.net/problem/2493

'''
미통과.

처음에는 queue를 사용하는걸로 잘못 생각했는데,
앞에서부터 순차적으로 값을 저장해두고 현재의 기준 값에서 가장 가까운 이전 값부터 탐색해야하므로 가장 나중에 추가된 값이 가장 먼저 나오는 stack을 사용해야한다.

핵심:
더 오른쪽에 있는 값이 더 높은 우선순위를 가지므로, stack[-1] < 현재 값이면 이후 탐색에서 어차피 더 오른쪽에 있고 더 큰 현재 값이 선택될것임.
따라서 이 경우 stack[-1]의 값은 필요없으므로 pop한다.
'''


N = int(input())
T = list(map(int, input().split()))
answer = [0] * N

# stack을 이용해 구현
# if stack[-1] >= 현재 값, 정답에 저장
# elif stack[-1] < 현재 값, 이후 값들에 대해서 어차피 더 오른쪽에 있는 현재 값이 선택될거기 때문에 stack[-1]를 pop
stack = []
for i in range(N):
    while stack:
        if stack[-1][0] >= T[i]:
            answer[i] = stack[-1][1]
        else:
            stack.pop()
    stack.append((T[i], i+1))
print(*answer)