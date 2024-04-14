# 백준 13305번 주유소 문제 (실버3)
# https://www.acmicpc.net/problem/13305

# 원 안의 숫자는 그 도시에서의 주유 비용
# 간선은 도시 간 거리
# return: 최소 전체 주유 비용


# --- 답안1. 최적의 코드 ---
N = int(input())    # 도시 수
dist = list(map(int, input().split()))      # 도시 간 거리
cost = list(map(int, input().split()))      # 도시 당 주유 비용

answer = 0
min_cost = cost[0]
for i in range(N-1):
    if cost[i] < min_cost:
        min_cost = cost[i]
    answer += min_cost * dist[i]
print(answer)


# --- 답안2. 시간 초과 코드 ---
# 아이디어: 그래프의 뒤에서부터 주유 비용이 최소인 곳을 찾고, 그곳부터 남은 거리를 모두 채우기를 반복
#
# N = int(input())  # 도시 수
# dist = list(map(int, input().split()))  # 도시 간 거리
# cost = list(map(int, input().split()))  # 도시 당 주유 비용
# cost.pop()
#
# answer = 0
# while len(dist) > 0:
#     min_cost = min(cost)
#     min_cost_idx = cost.index(min_cost)
#     left_dist = sum(dist[min_cost_idx:])  # 최소 주유 비용인 곳부터 남은 거리
#     answer += (min_cost * left_dist)
#
#     dist = dist[:min_cost_idx]
#     cost = cost[:min_cost_idx]
# print(answer)