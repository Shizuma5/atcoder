from fractions import gcd
from math import sqrt

# https://qiita.com/c-yan/items/36343c22ef8691421923
# sqrt(gcd(A, B))よりも大きい素数が一つだけあるため普通にループを回す

def prime_factorize(n):
    result = []
    for i in range(2, int(sqrt(n)) + 1):
        if n % i != 0:
            continue
        t = 0
        while n % i == 0:
            n //= i
            t += 1
        result.append((i, t))
        if n == 1:
            break
    if n != 1:
        result.append((n, 1))
    return result


A, B = map(int, input().split())
print(len(prime_factorize(gcd(A, B))) + 1)
