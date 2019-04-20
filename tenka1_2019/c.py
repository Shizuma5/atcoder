N = int(input())
S = input()

s = S.lstrip('.').rstrip('#')

w = s.count('.')
b = n - w

if w < b:
    print(w)
else:
    print(b)