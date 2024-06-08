# Codility Lesson 4 Counting Elements FrogRiverOne 문제 (Easy)
# https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/


'''
A[K]: the position where one leaf falls at time K
return: 0 -> X+1로 이동하는 earliest time (건널수없으면 -1)

1 ~ X가 모두 잎으로 덮여있어야함
O(NlogN)까지 가능
'''

# O(N)
def solution(X, A):
    finds = set(range(1, X+1))
    for idx in range(len(A)):
        finds.discard(A[idx])
        if not finds:
            return idx
    return -1