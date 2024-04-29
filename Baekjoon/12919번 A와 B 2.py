# 백준 12919번 A와 B 2 문제 (골드5)
# https://www.acmicpc.net/problem/12919

'''
처음에는 재귀를 활용해 S에서 T로 변형되도록 문자를 추가하는 방식으로 코드를 작성했는데, 시간 초과가 발생했다.
이유는 2번씩의 연산이 중첩되어 2의 배수로 늘어나기 때문이었다.
-> 그래서 T에서 S로 변형되도록 문자를 제거하는 방식으로 코드를 수정했더니 해결되었다.
'''


S = input()
T = input()
answer = 0

def dfs(T_new):
    global answer

    if len(T_new) == len(S):
        if T_new == S:
            answer = 1
        return

    if T_new[-1] == 'A':
        dfs(T_new[:-1])
    if T_new[0] == 'B' and answer == 0:
        dfs(T_new[1:][::-1])

dfs(T)
print(answer)