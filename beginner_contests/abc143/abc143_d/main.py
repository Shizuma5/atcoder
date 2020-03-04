import numpy as np

N = int(input())
L = np.array(list(map(int, input().split())))

ans = 0

L = np.sort(L)

for a in range(N-2):
    for b in range(a+1, N-1):
        ans += sum((L < (L[a]+L[b])) * (L > L[b]))

print(ans)
