# 백준 1541번 잃어버린 괄호 문제
# https://www.acmicpc.net/problem/1541

'''
가능한 글자: 0~9, +, -
결과를 최소로 만들기

연산자가 모두 + => 그대로
- 연산자 뒤에 나오는 +를 다 묶기
10 + 10 - (20 + 30 + 40) - 50
10 + 10 - 20 + 30 + 40 - 50
'''


# --- 답안1. 최적의 코드 ---
equation = input()
answer = 0
partitions = equation.split('-')
for i, part in enumerate(partitions):
    terms = part.split('+')
    if i==0:
        answer += sum(map(int, terms))
    else:
        answer -= sum(map(int, terms))
print(answer)


# --- 답안2. 한 글자씩 체크하여 좀 더 비효율적인 코드 ---
equation = input()
answer = 0
st = ""
is_minus = False
for ch in equation:
    if ch == '-':
        if is_minus:
            answer -= sum(map(int, st.split('+')))
        else:
            answer += sum(map(int, st.split('+')))
        st = ""
        is_minus = True
    else:
        st += ch
if st:
    if is_minus:
        answer -= sum(map(int, st.split('+')))
    else:
        answer += sum(map(int, st.split('+')))
print(answer)