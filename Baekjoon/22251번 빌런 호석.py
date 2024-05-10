# 백준 22251번 빌런 호석 문제 (골드5)
# https://www.acmicpc.net/problem/22251


# --- 나의 답안: 18위인걸보니 효율적으로 짠거같다 ㅎㅎ ---
def get_reverse_cnt(a, b):  # 반전시켜야하는 칸의 갯수
    return bin(LED[a] ^ LED[b])[2:].count('1')

def recursion(X_new, idx, left_cnt):
    global answer

    if idx == K:
        if X_new != X and 0 < int(X_new) <= N:
            answer += 1
        return

    num_org = int(X[idx])
    for num_new, cnt in enumerate(reverse_cnt[num_org]):
        if left_cnt - cnt >= 0:
            recursion(X_new + str(num_new), idx + 1, left_cnt - cnt)


N, K, P, X = map(int, input().split())
LED = ['1110111', '0010010', '1011101', '1011011', '0111010', '1101011', '1101111', '1010010', '1111111', '1111011']
LED = list(map(lambda x: int(x, 2), LED))   # 10진수로 변환
X = '0' * (K - len(str(X))) + str(X)
answer = 0

# reverse_cnt[i][j]: i를 j로 만들 때 반전시켜야 하는 횟수
reverse_cnt = [[] for _ in range(10)]
for i in range(10):
    for j in range(10):
        cnt = get_reverse_cnt(i, j)
        reverse_cnt[i].append(cnt)

recursion('', 0, P)
print(answer)