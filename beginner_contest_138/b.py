# python 3.4.3はgcdはfractionsの中

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


"""
以下例
そのまま計算しても良かったっぽい
"""
'''
N = int(input())
A = map(int, input().split())
print('{:.16g}'.format(1 / sum(1 / x for x in A)))
'''

