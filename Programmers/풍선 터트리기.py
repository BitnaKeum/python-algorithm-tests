# 프로그래머스 월간 코드 챌린지 시즌1 풍선 터트리기 문제 (Lv.3)
# https://school.programmers.co.kr/learn/courses/30/lessons/68646


# --- 답안1. 나의 답안 ---
'''
인접한 두 풍선 중 하나를 제거하기.
이때, 두 풍선 중 더 큰걸 제거해야하고, 더 작은걸 제거하는건 딱 1번만 가능.
return: a에서 최후에 남을 수 있는 풍선의 갯수

특정 풍선을 기준으로 왼쪽과 오른쪽에서 각각 최소값을 찾고, 둘 다 기준 풍선의 값보다 작으면 불가능.

점화식:
index i 풍선에 대해, (i==0일때는 따로, i>=1부터)
  if max(L[i-1], a[i], R[i+1]) == a[i]: 불가능
  else: 가능

L[i] = min(L[i-1], a[i])
R[i] = min(R[i+1], a[i])
R[i]를 먼저 싹 구해놓고, L[i]는 그때그때 연산하기.
'''
def solution(a):
    n = len(a)
    L = [0] * n # L[i]: index 0부터 i까지의 최소값
    R = [0] * n # R[i]: index n-1부터 i까지의 최소값
    L[0] = a[0]
    R[n - 1] = a[n - 1]

    # R 먼저 싹 구해놓기
    for i in range(n - 2, 0, -1):  # n-2 ~ 1
        R[i] = min(R[i + 1], a[i])

    answer = 2  # i == 0 or (n-1)일 때는 항상 가능하므로, answer = 2로 할당
    for i in range(1, n-1):
        L[i] = min(L[i - 1], a[i])
        if max(L[i - 1], a[i], R[i + 1]) != a[i]:
            answer += 1

    return answer


# --- 답안2. 최적의 답안 (다른사람의 풀이 참고) ---
'''
- 왼쪽부터 돌면서 내가 최소값이면 가능
- 나보다 왼쪽에 전체 최소값이 존재하는 경우에는 이 최소값에 대해 1번의 연산을 수행하고 내 오른쪽 값들이 다 나보다 크면 가능
=> 전체 최소값을 기준으로, 왼쪽 끝에서부터 전체 최소값 전까지 돌면서 최소값인지 확인 + 오른쪽 끝에서부터 전체 최소값 후까지 돌면서 최소값인지 확인
'''
def solution(a):
    answer = 1
    M = min(a)
    for _ in range(2):
        m = a[0]
        i = 1
        while m != M:
            if a[i] <= m:
                m = a[i]
                answer += 1
            i += 1
        a.reverse()

    return answer