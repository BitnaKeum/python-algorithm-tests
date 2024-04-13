# 프로그래머스 월간 코드 챌린지 시즌1 스타 수열 문제 (Lv.3)
#

'''
미통과. 너무 복잡하게 접근했음.

스타 수열:
- 길이가 짝수(=2n),
- 2개씩 묶어서 n개의 집합을 만들었을때, 모든 집합이 최소 1개의 동일한 원소를 포함
- 각 집합에 속한 두 원소는 서로 달라야 함
return:
주어진 배열 a의 부분 수열 중, 가장 길이가 긴 스타 수열의 길이
모든 부분 수열 중 스타 수열이 존재하지 않으면 0 반환
'''


# --- 최적의 답안 ---
from collections import Counter

def solution(a):
    answer = 0
    counts = Counter(a)  # Counter({값1: cnt1, 값2: cnt2, ...})
    if len(counts) == 1:  # a의 모든 값이 동일해서 스타 수열을 만들 수 없는 경우
        return 0

    for k in counts.keys():
        if counts[k] < answer // 2: # 현재의 k 값이 a에 등장한 횟수가 현재까지 구해진 스타수열에서의 횟수보다 작으면 스킵
            continue

        seq_len = 0
        i = 0
        while i < len(a) - 1:
            # ex: k가 0일 때
            if (a[i] == k or a[i + 1] == k) and a[i] != a[i + 1]:  # 스타 수열 O (ex: 03, 30)
                seq_len += 2
                i += 2
            else:  # 스타 수열 X (ex: 33, 35, 00)
                i += 1
        if seq_len > answer:
            answer = seq_len

    return answer