N = int(input())

strings = {}

ans = 0

for _ in range(N):
    s = sorted(list(input()))
    join_s = ''.join(s)
    if join_s in strings:
        strings[join_s] += 1
        ans += strings[join_s]
    else:
        strings[join_s] = 0

print(ans)