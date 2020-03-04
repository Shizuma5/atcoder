N = int(input())
D = list(map(int, input().split()))

ans = 0

for n in range(N):
    for i, d in enumerate(D):
        if i == n:
            continue
        else:
            ans += d * D[n]
print(int(ans/2))
