import sys
import math
def input():
    return sys.stdin.readline()[:-1]

N, D = map(int, input().split())

X = []

for n in range(N):
    X.append(list(map(int, input().split())))

def nolm(x, y):
    s = len(x)
    total = 0
    for i in range(s):
        total += (x[i] - y[i]) ** 2
    return math.sqrt(total)

ans = 0

for n in range(N-1):
    for i in range(n+1, N):
        if nolm(X[n], X[i]).is_integer():
            ans += 1

print(ans)
