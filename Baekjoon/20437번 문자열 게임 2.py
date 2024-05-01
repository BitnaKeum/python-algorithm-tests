'''
구할것:
- 어떤 문자를 K개 포함 && 첫 글자와 마지막 글자가 해당 문자로 같은 가장 짧은 연속 문자열의 길이
- 어떤 문자를 K개 포함 && 첫 글자와 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열의 길이
=> 어떤 문자를 K개 포함 && 첫 글자와 마지막 글자가 해당 문자로 같은 문자열의 길이를 모두 리스트에 저장한 후, 최소값과 최대값 반환하기
'''

# --- 답안1. 시간 단축시킨 코드 (참고) ---
# 문자열 W를 순차적으로 돌면서 find() 연산 필요없이 index를 저장하여 시간 단축
T = int(input())
for _ in range(T):
    W, K = input().rstrip(), int(input())

    # 문자열을 구성하는 고유한 문자들을 구한 후, 각 문자마다 등장한 index를 해시테이블에 저장
    hash_table = {ch: [] for ch in set(list(W))}
    for i, ch in enumerate(W):
        hash_table[ch].append(i)

    # 어떤 문자가 K번 등장한 문자열의 길이를 lengths 배열에 저장
    lengths = []
    for idxes in hash_table.values():
        if len(idxes) >= K:
            for i in range(len(idxes) - K + 1):
                lengths.append(idxes[i + K - 1] - idxes[i] + 1)

    # 결과 출력
    if lengths:
        print(min(lengths), max(lengths))
    else:
        print(-1)


# --- 답안2. 처음 작성한 답안 ---
# 각 문자마다 등장한 index를 찾는 과정에서 find() 연산을 반복적으로 수행해서 소요 시간 증가
# T = int(input())
# inputs = [(input(), int(input())) for _ in range(T)]
# for W, K in inputs:
#     hash_table = {}
#     lengths = []
#
#     # 문자열을 구성하는 고유한 문자들을 구한 후, 각 문자마다 등장한 index를 해시테이블에 저장
#     for ch in set(list(W)):
#         hash_table[ch] = list()
#         i = -1
#         while True:
#             i = W.find(ch, i+1)
#             if i == -1:
#                 break
#             hash_table[ch].append(i)
#
#     # 어떤 문자가 K번 등장한 문자열의 길이를 lengths 배열에 저장
#     for ch, idxes in hash_table.items():
#         if len(idxes) < K:
#             continue
#         for i in range(len(idxes)-K+1):
#             length = idxes[i+K-1] - idxes[i] + 1
#             lengths.append(length)
#
#     # 결과 출력
#     if lengths:
#         print(min(lengths), max(lengths))
#     else:
#         print(-1)