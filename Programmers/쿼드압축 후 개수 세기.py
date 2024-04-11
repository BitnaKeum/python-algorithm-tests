# 프로그래머스 월간 코드 챌린지 시즌1 쿼드압축 후 개수 세기 문제 (Lv.2)
# https://school.programmers.co.kr/learn/courses/30/lessons/68936


# --- 답안1. 최적의 답안 ---
# 전체 배열에 덧셈 연산을 수행하지 않고, 모든 값을 순회하면서 첫번째 값과 다른 값이 하나라도 있을 경우 바로 압축 불가로 판단
def solution(arr):
    answer = [0, 0]  # [zero_cnt, one_cnt]

    def recursion(s_row, s_col, cur_len):
        if cur_len == 1:  # 종료 조건
            answer[arr[s_row][s_col]] += 1
            return

        first_value = arr[s_row][s_col]
        for row in range(s_row, s_row + cur_len):
            for col in range(s_col, s_col + cur_len):
                if arr[row][col] != first_value:  # 압축 X
                    cur_len = cur_len // 2
                    recursion(s_row, s_col, cur_len)
                    recursion(s_row, s_col + cur_len, cur_len)
                    recursion(s_row + cur_len, s_col, cur_len)
                    recursion(s_row + cur_len, s_col + cur_len, cur_len)
                    return
        answer[first_value] += 1  # 압축 O

    recursion(0, 0, len(arr))

    return answer


# --- 답안2. 나의 답안 ---
# 전체 배열에 덧셈 연산을 수행한 후에 압축 여부를 따졌기 때문에 코드가 좀 더 길어짐
def solution(arr):
    answer = [0, 0]  # [zero_cnt, one_cnt]

    def recursion(s_row, s_col, cur_len):
        if cur_len == 1:  # 종료 조건
            answer[arr[s_row][s_col]] += 1
            return

        sum_result = 0
        for row in range(s_row, s_row + cur_len):
            for col in range(s_col, s_col + cur_len):
                sum_result += arr[row][col]
        if sum_result == 0:  # 압축 O
            answer[0] += 1
            return
        elif sum_result == cur_len ** 2:  # 압축 O
            answer[1] += 1
            return
        else:  # 압축 X
            cur_len = cur_len // 2
            recursion(s_row, s_col, cur_len)
            recursion(s_row, s_col + cur_len, cur_len)
            recursion(s_row + cur_len, s_col, cur_len)
            recursion(s_row + cur_len, s_col + cur_len, cur_len)

    recursion(0, 0, len(arr))

    return answer