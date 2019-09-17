import numpy as np
import sys
def input():
    return sys.stdin.readline()[:-1]

N, K, Q = map(int, input().split())

points = np.array([K - Q for _ in range(N)])

for q in range(Q):
    A = int(input()) - 1
    points[A] +=1

for p in points:
    if p < 1:
        print('No')
    else:
        print('Yes')
