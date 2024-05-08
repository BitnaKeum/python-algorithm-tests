# 백준 2668번 숫자고르기 문제 (골드5)
# https://www.acmicpc.net/problem/2668

'''
반례:

1 2 3 4 5
3 4 1 5 2
-> 5개

1 2 3 4
3 1 4 2
-> 4개

1 2 3 4
3 1 4 1
-> 3개

1 2 3 4 5
2 3 4 5 5
-> 1개

1 2 3
2 3 2
-> 2개
'''



# --- 답안1. 빡 구현 ---
# 첫째줄과 둘째줄에서 방문한 원소들을 각각의 set에 저장하면서,
# 맨 처음 방문한 첫째줄의 원소(start_node)로 다시 돌아오는(순환) 경우를 찾음
N = int(input())
second = [-1] + [int(input()) for _ in range(N)]

res1, res2 = set(), set()
for start_node in range(1, N + 1):
    if start_node in res1 or second[start_node] in res2:
        continue
    # 좀더 효율적으로 연산하려고 넣은 코드인데, 어차피 N의 범위가 작아서 안넣어도 됨
    #if start_node > second[start_node] and second[start_node] not in res1:
    #    continue
    if start_node == second[start_node]:
        res1.add(start_node)
        res2.add(start_node)
        continue

    node = start_node
    temp1, temp2 = res1.copy(), res2.copy()
    while True:
        if node not in temp1 and second[node] not in temp2:
            temp1.add(node)
            temp2.add(second[node])
            node = second[node]
            if node == start_node:
                res1, res2 = temp1.copy(), temp2.copy()
                break
        else:
            break

print(len(res1))
for node in sorted(res1):
    print(node)


# --- 답안2. 재귀 이용 ---
# 재귀를 이용해, 맨 처음 방문한 첫째줄의 원소(start_node)로 다시 돌아오는(순환) 경우를 찾음
N = int(input())
second = [-1] + [int(input()) for _ in range(N)]
visited = [False] * (N + 1)
result = []

def dfs(node, visited_new, temp):
    global start_node, visited

    visited_new[node] = True
    temp.append(node)

    next_node = second[node]
    if next_node == start_node:
        result.extend(temp)
        visited = visited_new[::]
        return
    elif visited_new[next_node]:
        return
    dfs(next_node, visited_new, temp)

for i in range(1, N + 1):
    if not visited[i]:
        start_node = i
        dfs(start_node, visited[::], [])

print(len(result))
for i in sorted(result):
    print(i)


# --- 답안3. 재귀 이용. 최적의 코드 (참고) ---
# 답안2와 차이점:
# - 각 start node에 대해 반복할 때마다 visited 배열을 새로 초기화하여 사용하고, 순환된 경우에 start node만 결과 리스트에 저장하기 때문에 코드가 더 깔끔해짐
# - dfs() 함수 내에서, 답안2에서는 종료 조건 먼저 나열해서 return문이 필요하지만 답안3에서는 재귀함수 실행 조건 먼저 나열하여 return문이 불필요
N = int(input())
second = [-1] + [int(input()) for _ in range(N)]
result = []

def dfs(node, start_node):
    visited[node] = True
    next_node = second[node]
    if not visited[next_node]:
        dfs(next_node, start_node)
    elif next_node == start_node:
        result.append(start_node)

for i in range(1, N + 1):
    visited = [False] * (N + 1)
    dfs(i, i)

print(len(result))
for i in sorted(result):
    print(i)