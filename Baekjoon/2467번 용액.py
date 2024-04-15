# 백준 2467번 용액 문제 (골드5)
# https://www.acmicpc.net/problem/2467

'''
단순 투 포인터를 활용하는 문제이기 때문에 체감상 골드5 난이도보다 낮은 것 같다.
'''


N = int(input())  # 용액의 수
f = list(map(int, input().split()))

if f[0] > 0:  # 모든 특성값이 양수
    print(f[0], f[1])
elif f[N - 1] < 0:  # 모든 특성값이 음수
    print(f[N - 2], f[N - 1])
else:
    # 투 포인터
    left, right = 0, N - 1
    memory_sum = 2000000000
    while left < right:
        cur_sum = f[left] + f[right]

        if abs(cur_sum) < memory_sum:
            num1, num2 = f[left], f[right]
            memory_sum = abs(cur_sum)

        if cur_sum > 0:
            right -= 1
        elif cur_sum < 0:
            left += 1
        else:
            break

    print(num1, num2)