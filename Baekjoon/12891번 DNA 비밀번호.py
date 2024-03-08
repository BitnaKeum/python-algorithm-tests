# 백준 12891번 DNA 비밀번호 문제 (실버2)
# https://www.acmicpc.net/problem/12891

'''
슬라이딩 윈도우 활용 문제
'''

s, p = map(int, input().split())
dna = input()
a_min, c_min, g_min, t_min = map(int, input().split())

answer = 0
cnt = {}
for i in range(s - p + 1):
    if i == 0:
        password = dna[:p]
        for ch in ['A', 'C', 'G', 'T']:
            cnt[ch] = password.count(ch)
    else:
        prev_ch = dna[i - 1]
        new_ch = dna[i + p - 1]
        cnt[prev_ch] -= 1
        cnt[new_ch] += 1

    if cnt['A'] >= a_min and cnt['C'] >= c_min and cnt['G'] >= g_min and cnt['T'] >= t_min:
        answer += 1
print(answer)