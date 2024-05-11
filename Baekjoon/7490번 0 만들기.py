# 백준 7490번 0 만들기 문제 (골드5)
# https://www.acmicpc.net/problem/7490


# --- 답안1. 효율적인 코드 ---
# 방정식을 만들면서 결과값 계산도 함께 수행하도록 수정 => 효율성 증가
def make_equation(eq, idx, result, sign, num):
    global answers

    num = num * 10 + idx
    # new_result = result + num if sign == '+' else result - num
    new_result = result + (num if sign == '+' else -num)    # 원래 위 line처럼 작성했었는데, 이렇게 작성하는 법을 배웠다
    if idx == N:
        if new_result == 0:
            answers.append(eq + str(idx))
        return

    make_equation(eq + str(idx) + ' ', idx + 1, result, sign, num)
    make_equation(eq + str(idx) + '+', idx + 1, new_result, '+', 0)
    make_equation(eq + str(idx) + '-', idx + 1, new_result, '-', 0)


T = int(input())
for _ in range(T):
    N = int(input())
    answers = []
    make_equation(eq='', idx=1, result=0, sign='+', num=0)
    for answer in sorted(answers):
        print(answer)
    print()


# --- 답안2. 처음 작성한 코드 ---
# 방정식을 만드는 함수와 방정식이 완성된 후 결과값을 계산하는 함수를 별도로 선언 => 효율성 감소
def get_result(eq):
    result = 0
    sign, num = '+', 0
    for x in eq + '+':
        if '1' <= x <= '9':
            num += int(x)
        elif x == ' ':
            num *= 10
        else:
            if sign == '+':
                result += num
            else:
                result -= num
            num = 0
            sign = x

    return result

def make_equation(eq, num):
    global answers

    if num == N:
        eq += str(num)
        if get_result(eq) == 0:
            answers.append(eq)
        return
    make_equation(eq + str(num) + '+', num + 1)
    make_equation(eq + str(num) + '-', num + 1)
    make_equation(eq + str(num) + ' ', num + 1)


T = int(input())
for _ in range(T):
    N = int(input())

    answers = []
    make_equation('', 1)
    for answer in sorted(answers):
        print(answer)
    print()