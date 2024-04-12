'''
10 -> 11
100 -> 101
1010 -> 1011
일의자리가 0이면, 일의자리를 1로 만들면 됨

1001 -> 1010
1011 -> 1101
0111 -> 1011
10101 -> 10110
10111 -> 11011
101111 -> 110111
00111111 -> 01011111
일의자리가 1이면, 뒤에서부터 연속된 가장 앞 1을 0으로, 그 앞자리의 0을 1로 만들기
'''


def convert_to_binary(num):  # 10진법 -> 2진법
    # binary = ''
    # while num > 0:
    #     binary += str(num % 2)  # '0' or '1'
    #     num = num // 2
    # return '0' + binary[::-1]  # num:8 -> return '01000'
    return '0' + bin(num)[2:]


def convert_to_ten(binary):  # 2진법 -> 10진법
    return int(binary, 2)


def solution(numbers):
    answer = []

    for num in numbers:
        binary = convert_to_binary(num)  # '01000'
        if binary[-1] == '0':
            binary = binary[:-1] + '1'  # 일의자리를 '1'로
        else:
            i = len(binary) - 1
            while binary[i] == '1':  # 연속된 가장 앞 1 찾기
                i -= 1
            # i번째 위치를 '1'로, (i+1)번째 위치를 '0'으로
            binary = binary[:i] + '10' + binary[i + 2:]
        answer.append(convert_to_ten(binary))
        print(binary)

    return answer