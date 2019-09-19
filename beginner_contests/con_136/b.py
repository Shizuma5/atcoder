import sys
def input():
    return sys.stdin.readline()[:-1]

N = int(input())

digit = len(str(N))

if digit == 1:
    ans = N
elif digit == 2:
    ans = 9
elif digit == 3:
    ans = N - 99 + 9
elif digit == 4:
    ans = 909
elif digit == 5:
    ans = N - 9999 + 900 + 9
elif digit == 6:
    ans = 90000 + 900 + 9

print(ans)