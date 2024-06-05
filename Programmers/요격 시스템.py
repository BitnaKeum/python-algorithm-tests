# 프로그래머스 연습문제 요격 시스템 (Lv.2)
# https://school.programmers.co.kr/learn/courses/30/lessons/181188

'''
리스트를 정렬할 때 당연하게 시작 지점(s)을 기준으로 정렬해야 한다고 생각했다.
하지만 이 문제의 핵심은 끝 지점(e)을 기준으로 정렬하는 것이었다.
그런데 왜 시작 지점을 기준으로 정렬해서 풀면 안되는지 명확히 이해가 안됐다... (=> 7개 케이스가 틀림)

사실 그렇게 어렵지는 않은 문제인데 너무 어렵게 이해한 경향이 있다.
문제풀이의 필요성을 또 한번 깨닫는다.
'''


# --- 답안1. 최적의 코드 ---
def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])
    e = 0
    for target in targets:
        s = target[0]
        if e <= s:
            e = target[1]
            answer += 1

    return answer


# --- 답안2. 내가 작성한 코드 ---
# 정렬을 x[1] 기준으로 안하고 x[0] 기준으로 해서 틀림
# pop()을 여러번 호출해야해서 deque 자료형을 사용했는데 굳이 안써도 됐다

from collections import deque

def solution(targets):
    answer = 0
    q = deque(sorted(targets, key=lambda x: x[1]))
    while q:
        s, e = q[0]
        idx = 1
        while idx < len(q):
            if q[idx][0] >= e:
                break
            idx += 1
        answer += 1
        for _ in range(idx):
            q.popleft()

    return answer