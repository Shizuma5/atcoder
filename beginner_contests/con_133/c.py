import sys
def input():
    return sys.stdin.readline()[:-1]

L, R = map(int, input().split())

if L == 0:
    print(0)
    sys.exit()

def calc(l, r):
    return ((l % 2019) * (r % 2019)) % 2019

diff = R - L + 1


ans = calc(L, L+1)

dp = [[calc(L+i, L+i+1)] for i in range(diff-1)]

for l in range(diff-1):
    for r in range(1, diff):
        dp[l][r] = (dp[l][0] * r) % 2019
        if ans > dp[l][r]:
            ans = dp[l][r]

print(ans)
