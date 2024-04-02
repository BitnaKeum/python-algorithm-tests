# 프로그래머스 월간 코드 챌린지 2 110 옮기기 문제 (Lv.3)
# https://school.programmers.co.kr/learn/courses/30/lessons/77886#

'''
미통과. 유형을 분류하자면 그리디 알고리즘 유형의 문제.

풀이:

"110"을 뽑아서 다시 삽입한 후, 삽입된 부분과 기존 부분이 합쳐지면서 새로운 "110"이 생길 수는 없음
-> 한번 뽑고 삽입하는 걸 반복하지 말고, 한번에 모든 "110"을 뽑자
-> 한번 뽑은 다음에는 문자열이 변형되므로 list comprehension을 사용할 수 없음
-> stack을 이용하자

"110" 삽입할 위치를 파악해보자
    000#1111111
    00010#
    000100#1
    000100#11
    000100#111
    #11111
위의 경우를 통해 규칙을 찾을 수 있다. (#이 삽입할 위치)
 - 마지막으로 나온 0 뒤에
 - 0이 없으면 맨 앞에
'''


def solution(s):
    answer = []
    for x in s:

        # x로부터 모든 "110" 뽑기
        stack = []
        target_cnt = 0
        for i in range(len(x)):
            if x[i] == "1":
                stack.append(x[i])
            else:  # x[i] == "0"
                if len(stack) >= 2 and stack[-1] == "1" and stack[-2] == "1":  # "110"
                    stack.pop()
                    stack.pop()
                    target_cnt += 1
                else:
                    stack.append(x[i])

        # "110" 삽입할 위치 찾기
        # 마지막으로 나온 0 뒤에, 0이 없으면 맨 앞에
        x = "".join(stack)
        last_zero_idx = x.rfind("0")
        if last_zero_idx != -1:
            x = x[:last_zero_idx + 1] + "110" * target_cnt + x[last_zero_idx + 1:]
        else:
            x = "110" * target_cnt + x
        answer.append(x)

    return answer