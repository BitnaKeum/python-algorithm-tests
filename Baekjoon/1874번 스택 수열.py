# 백준 1874번 스택 수열 (실버2)
# https://www.acmicpc.net/problem/1874

'''
스택 활용 문제
'''

# --- 답안1. 효율적인 답안 ---
def solution(target, n):
    source_num = 1
    result = []
    stack = []
    for target_num in target:
        while True:
            if stack and stack[-1] == target_num:
                stack.pop()
                result.append("-")
                break
            else:
                if source_num > n:
                    return "NO"
                stack.append(source_num)
                source_num += 1
                result.append("+")
    return "\n".join(result)

n = int(input())
target = []
for _ in range(n):
    target.append(int(input()))
print(solution(target, n))


# --- 답안2. 조금 더 비효율적인 답안 ---
# 오름차순 정렬을 따로 만들어서 비효율적
def solution(target, n):
    source = sorted(target, reverse=True)
    result = []
    stack = []
    for target_num in target:
        while True:
            if stack and stack[-1] == target_num:
                stack.pop()
                result.append("-")
                break
            else:
                if not source:
                    return "NO"
                source_num = source.pop()
                stack.append(source_num)
                result.append("+")
    return "\n".join(result)

n = int(input())
target = []
for _ in range(n):
    target.append(int(input()))
print(solution(target, n))