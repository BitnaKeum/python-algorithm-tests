# 백준 20922번 겹치는 건 싫어 문제 (실버1)
# https://www.acmicpc.net/problem/20922

'''
미통과. LCS 문제가 생각나서 DP로 풀어보려 했는데 점화식 세우기 실패함.

투 포인터 활용 문제.
return: 동일한 원소가 K개 이하로 들어있는 가장 긴 연속 부분 수열의 길이
'''


N, K = map(int, input().split())
seq = list(map(int, input().split()))

# 투 포인터
cnt = {num: 0 for num in set(seq)}
cnt[seq[0]] = 1    # 첫번째 원소 카운트
answer = cur_len = 1
start, end = 0, 1
while end < N:
# while start <= end and end < N:
    if cnt[seq[end]] < K:
        cnt[seq[end]] += 1
        end += 1
        cur_len += 1
    else:    # 특정 원소가 K+1번 등장한 경우
        cnt[seq[start]] -= 1
        start += 1
        cur_len -= 1
    answer = max(answer, cur_len)
print(answer)