# 백준 9252번 LCS 2 문제 (골드4)
# https://www.acmicpc.net/problem/9252

'''
동적 계획법 활용 문제.
전형적인 LCS 문제라고 하는데, 익숙치 않은 유형이라 통과하지 못했다. 잘 익혀두자!

arr
- C A P C A K (seq2)
A
C
A
Y
K
P
(seq1)
'''


seq1 = [''] + list(input())
seq2 = [''] + list(input())

row, col = len(seq1), len(seq2)
arr = [[0 for _ in range(col)] for _ in range(row)]
for i in range(1, row):
    for j in range(1, col):
        if seq1[i] == seq2[j]:
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])

# if arr[row-1][col-1] != 0:    # 문제에서 'LCS의 길이가 0인 경우에는 둘째 줄을 출력하지 않는다.' 부분을 처리하기 위해 하단의 코드를 if문 안에 넣었었는데 95%에서 틀렸었다.
lcs_len = arr[row-1][col-1]
print(lcs_len)  # LCS 길이 출력

lcs = ''
i, j = row-1, col-1
while i > 0 and j > 0:
    if seq1[i] == seq2[j]:
        lcs = seq1[i] + lcs
        if len(lcs) == lcs_len:
            print(lcs)  # LCS 출력
            break
        i -= 1
        j -= 1
    else:
        if arr[i-1][j] > arr[i][j-1]:
            i -= 1
        else:
            j -= 1