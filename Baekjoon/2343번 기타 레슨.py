# 백준 2343번 기타 레슨 문제 (실버1)
# https://www.acmicpc.net/problem/2343


'''
블루레이 M개에 N개의 강의를 넣어야하고, 이때 한 블루레이의 최소 길이를 구하는 문제.
입력 값의 범위를 보니 O(nlogn)의 시간복잡도를 갖는 알고리즘 사용 가능. -> 이진 탐색 !

당연스럽게 주어진 레슨 배열에 대해 이진 탐색을 수행하려고 했는데, 찾으려는 target 설정이 어렵고 또 종료 조건 설정도 어려웠음.
또한, 레슨 배열은 문제 조건에 따르면 입력된 순서를 유지해야하는데 정렬이 안되어있을 수도 있음
-> 그러면 레슨 배열에 이진 탐색을 적용하는게 아니구나
-> 그러면 우리가 찾으려는게 블루레이의 크기 이므로 크기의 범위에 대해서 이진탐색을 적용하면 되겠구나!
   블루레이의 크기 범위: 제일 긴 레슨 길이 ~ 모든 레슨의 길이 합
'''


n, m = map(int, input().split())
lectures = list(map(int, input().split()))


def binary_search(start, end):
    candidates = []
    while start <= end:
        mid = (start + end) // 2

        # 현재 블루레이 크기(mid)와 블루레이 갯수(m)에 모든 레슨을 저장할 수 있는지 확인
        cur_cnt = 1
        cur_length = 0
        for lecture in lectures:
            if cur_length + lecture > mid:
                cur_cnt += 1
                cur_length = 0
            cur_length += lecture

        if cur_cnt <= m:  # 블루레이 크기 줄이기
            end = mid - 1
            candidates.append(mid)
        else:  # 블루레이 크기 늘리기
            start = mid + 1
    return min(candidates)


print(binary_search(max(lectures), sum(lectures)))