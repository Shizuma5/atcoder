import sys
def input():
    return sys.stdin.readline()[:-1]

N = int(input())

H = list(map(int, input().split()))

for i in range(N - 2, 0, -1):
    if H[i] > H[i + 1]:
        H[i] -= 1
    if H[i] > H[i + 1]:
        print('No')
        sys.exit()
print('Yes')
