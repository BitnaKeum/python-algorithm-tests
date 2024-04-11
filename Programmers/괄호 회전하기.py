# 프로그래머스 월간 코드 챌린지 시즌2 괄호 회전하기 문제 (Lv.2)
# https://school.programmers.co.kr/learn/courses/30/lessons/76502?language=python3

'''
괄호 쌍 맞추기 문제는 stack 활용!

s = "()[{}]" 인 경우를 참고

핵심:
- 여는 괄호가 연속적으로 나오는건 ok
- 닫는 괄호가 나왔을 때는 해당 종류의 여는 괄호가 여태까지 등장한 여는 괄호 중 가장 마지막에 등장했어야함
  -> 여는 괄호가 등장하면 stack에 저장하고, 닫는 괄호가 등장하면 stack.pop()해서 비교하기
'''


def solution(s):
    answer = 0
    pair = {
        "]": "[",
        ")": "(",
        "}": "{"
    }
    for x in range(len(s)): # s를 x칸만큼 회전
        s_rotated = s[x:] + s[:x]
        stack = []
        is_correct = True
        for p in s_rotated:
            if p not in pair:   # 여는 괄호이면, stack에 저장
                stack.append(p)
            else:   # 닫는 괄호이면, stack의 맨 위 값이 해당 종류의 여는 괄호여야 함
                if not stack or stack.pop() != pair[p]:   # 올바른 괄호 문자열 X
                    is_correct = False
                    break
        if not stack and is_correct:    # 쌍이 다 맞았다면 stack이 비어있어야 함
            answer += 1

    return answer