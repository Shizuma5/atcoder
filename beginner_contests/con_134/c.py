import sys
def input():
    return sys.stdin.readline()[:-1]

N = int(input())

max_num = 0
max_index = 0
second_num = 0
for i in range(N):
    num = int(input())
    if num >= max_num:
        if second_num < 1:
            max_num = num
            second_num = 1
        else:
            second_num, max_num = max_num, num
        max_index = i
    elif num > second_num:
        second_num = num
for i in range(N):
    if max_index == i:
        print(second_num)
    else:
        print(max_num)
