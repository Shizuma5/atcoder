import sys
def input():
    return sys.stdin.readline()[:-1]

A, B = map(int, input().split())

if (A + B) % 2 == 1 or A == B:
    print('IMPOSSIBLE')
else:
    print(int((A+B)/2))