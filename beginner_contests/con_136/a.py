import sys
def input():
    return sys.stdin.readline()[:-1]

A, B, C = map(int, input().split())

ans = B+C-A

if ans < 0:
    print(0)
else:
    print(ans)