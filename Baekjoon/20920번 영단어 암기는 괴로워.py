# 백준 20920번 영단어 암기는 괴로워 문제 (실버3)
# https://www.acmicpc.net/problem/20920



# --- 답안 ---
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

words_cnt = {}
for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:
        if word not in words_cnt:
            words_cnt[word] = 1
        else:
            words_cnt[word] += 1

# words_cnt의 key <-> value 바꾸기
cnt_words = {}
for word in words_cnt.keys():
    cnt = words_cnt[word]
    if cnt not in cnt_words:
        cnt_words[cnt] = [word]
    else:
        cnt_words[cnt].append(word)

for cnt in sorted(cnt_words.keys(), reverse=True):
    words = cnt_words[cnt]
    for word in sorted(words, key=lambda x: (-len(x), x)):
        print(word)