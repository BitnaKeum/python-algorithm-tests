# 프로그래머스 월간 코드 챌린지 시즌1 이진 변환 반복하기 문제 (Lv.2)
# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    convert_cnt, rm_zero_cnt = 0, 0

    while s != "1":
        rm_zero_cnt += s.count('0')
        s = bin(s.count('1'))[2:]
        convert_cnt += 1

    return [convert_cnt, rm_zero_cnt]