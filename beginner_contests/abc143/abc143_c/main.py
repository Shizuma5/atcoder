N = int(input())
S = list(input())

ans = ''

cache = ''

for s in S:
    if cache == '':
        ans += s
        cache = s
        continue
    if cache == s:
        continue
    else:
        ans += s
        cache = s

print(len(ans))
