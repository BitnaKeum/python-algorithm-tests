# 백준 20055번 컨베이어 벨트 위의 로봇 문제 (골드5)
# https://www.acmicpc.net/problem/20055

'''
내리는 위치의 로봇을 처리하는 게 조금 까다로웠다. 구현하는 데에 1시간 10분정도 걸렸음.
'''


# --- 답안1. 최적의 코드 ---
from collections import deque

N, K = map(int, input().split())

belt = deque([False] * (2 * N))
A = deque(list(map(int, input().split())))
step = 1

while True:
    # process 1
    # 벨트를 로봇과 함께 한 칸 회전
    belt.rotate(1)
    A.rotate(1)
    belt[N - 1] = False  # 내리는 위치에 있는 로봇 내리기

    # process 2
    # 벨트에 올라간 순서대로, 로봇의 이동 가능 여부 검사
    #    if 다음 칸에 로봇이 없음 && 다음 칸의 내구도 > 0 이면, 이동 가능
    for i in range(N - 2, -1, -1):
        if belt[i] and not belt[i + 1] and A[i + 1] > 0:  # 이동 가능
            A[i + 1] -= 1
            belt[i] = False
            belt[i + 1] = True
    belt[N - 1] = False  # 내리는 위치에 있는 로봇 내리기

    # process 3
    # 올리는 위치에 로봇 올리기 (내구도 > 0 이면)
    if A[0] > 0:
        A[0] -= 1
        belt[0] = True

    # process 4
    # if 내구도가 0인 칸의 수 >= K이면, 종료
    if A.count(0) >= K:
        break

    step += 1

print(step)


# --- 답안2. 내가 작성한 코드 ---
# belt를 벨트의 인덱스용으로, robot을 벨트 위 로봇 유무를 나타내는 용으로 따로 선언했는데, 하나의 리스트로 합치는 것이 효율적임
from collections import deque

N, K = map(int, input().split())

belt = deque(list(range(2 * N)))
A = deque(list(map(int, input().split())))
robot = deque([0] * N)
step = 1

while True:
    # process 1
    # 벨트를 로봇과 함께 한 칸 회전
    belt.rotate(1)
    A.rotate(1)
    robot.pop()
    robot.appendleft(0)
    robot[N - 1] = 0  # 내리는 위치에 있는 로봇 내리기

    # process 2
    # 벨트에 올라간 순서대로, 로봇의 이동 가능 여부 검사
    #    if 다음 칸에 로봇이 없음 && 다음 칸의 내구도 > 0 이면, 이동 가능
    for i in range(N - 2, -1, -1):
        if robot[i] == 1 and robot[i + 1] == 0 and A[i + 1] > 0:  # 이동 가능
            A[i + 1] -= 1
            robot[i] = 0
            robot[i + 1] = 1
            robot[N - 1] = 0  # 내리는 위치에 있는 로봇 내리기

    # process 3
    # 올리는 위치에 로봇 올리기 (내구도 > 0 이면)
    if A[0] > 0:
        A[0] -= 1
        robot[0] = 1

    # process 4
    # if 내구도가 0인 칸의 수 >= K이면, 종료
    if A.count(0) >= K:
        break

    step += 1

print(step)