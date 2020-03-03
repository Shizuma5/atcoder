import numpy as np
import copy as cp

def common_divisors(m, n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if m % i == 0 and n % i == 0:
            divisors.append(i)
            if i != m // i and i != n // i:
                divisors.append(n//i)
    return divisors

A, B = map(int, input().split())

divisors = np.array(sorted(common_divisors(A, B)))

ans = cp.deepcopy(divisors)

no_ans = []

for d in divisors:
    if d in no_ans or d == 1:
        continue
    ans = ans[ans % d != 0]
    no_ans += list(divisors[divisors % d == 0])
    ans = np.append(ans, d)
    ans.sort()
print(len(ans))
