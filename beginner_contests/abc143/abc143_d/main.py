N = int(input())
L = list(map(int, input().split()))

ans = 0

for a in range(N):
    for b in range(a+1, N):
        for c in range(b+1, N):
            if L[a] < L[b] + L[c] and L[b] < L[c] + L[a] and L[c] < L[a] + L[b]:
                ans += 1

print(ans)
