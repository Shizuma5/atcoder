import sys
def input():
    return sys.stdin.readline()[:-1]

N = int(input())
P = list(map(int, input().split()))

miss_count = 0

for i, p in enumerate(P, start=1):
    if not i == p:
        miss_count += 1

    if miss_count > 2:
        print('NO')
        sys.exit()
print('YES')