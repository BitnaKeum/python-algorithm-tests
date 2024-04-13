# 백준 1406번 에디터 문제 (실버2)
# https://www.acmicpc.net/problem/1406



### 문자열 자르고 더하는 연산은 시간복잡도가 O(n)이기 때문에 전체 시간복잡도가 O(n^2)여서 시간초과 발생!! 다시 풀기

import sys
input = sys.stdin.readline.rstrip

seq = input()
M = int(input())
cursor = len(seq)  # 문자열 맨 뒤에 위치

for _ in range(M):
    cmd = input()

    if cmd == "L":  # 왼쪽으로 한칸 옮기기
        cursor = max(cursor - 1, 0)
    elif cmd == "D":  # 오른쪽으로 한칸 옮기기
        cursor = min(cursor + 1, len(seq))
    elif cmd == "B":  # 왼쪽 문자 하나 삭제
        if cursor > 0:
            # seq = 'abc'
            # seq[cursor - 1] 문자를 삭제, cursor -= 1
            seq = seq[:cursor - 1] + seq[cursor:]
            cursor -= 1
    else:  # insert_ch 문자를 왼쪽에 추가
        cmd, insert_ch = cmd.split()
        seq = seq[:cursor] + insert_ch + seq[cursor:]
        cursor += 1
print(seq)