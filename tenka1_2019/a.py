a, b, c = map(int, input().split(' '))

if a > b and b > c and a > c:
    print('No')
if a > c and a > b and c > b:
    print('Yes')
elif b > a and b > c and a > c:
    print('No')
elif b > c and c > a and b > a:
    print('Yes')
elif c > a and c > b and a > b:
    print('No')
elif  c > b and c > a and b > a:
    print('No')