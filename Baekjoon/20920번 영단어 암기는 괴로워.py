# 백준 20920번 영단어 암기는 괴로워 문제 (실버3)
# https://www.acmicpc.net/problem/20920


# --- 답안1. 최적의 코드 (참고) ---
# Counter 모듈 사용
import sys
input = sys.stdin.readline
from collections import Counter

N, M = map(int, input().split())

words = []
for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:
        words.append(word)

words_count = Counter(words)

words = sorted(words_count)
words = sorted(words, key=len, reverse=True)
words = sorted(words, key=words_count.get, reverse=True)

print("\n".join(words))


# --- 답안2. 나의 개선한 코드 ---
# 딕셔너리 정렬
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

word_cnt = {}
for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:
        if word not in word_cnt:
            word_cnt[word] = 1
        else:
            word_cnt[word] += 1

for word, cnt in sorted(word_cnt.items(), key=lambda x: (-x[1], -len(x[0]), x[0])):
    print(word)


# --- 답안3. 나의 처음 작성한 코드 ---
# 딕셔너리 정렬이 익숙치 않아서 리스트 정렬을 하려다보니 코드가 길어짐
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