# python 3.4.3はgcdはfractionsの中
# でかい数で割るときは工夫すべし

import numpy as np
from fractions import gcd
from functools import reduce

def gcd_list(numbers):
    return reduce(gcd, numbers)

n = int(input())

a = list(map(int, input().split(' ')))

devisor = gcd_list(a)

a = np.array(a) / devisor
child = a.prod()
child *= devisor

mother = 0

for m in range(n):
    mother += np.delete(a, m).prod()

x = child / mother

print(x)
