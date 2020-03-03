import math
import sys
import numpy as np

def input():
    return sys.stdin.readline()[:-1]

N = int(input())
A = np.array(list(map(int, input().split())))

ans = [0] * (N+1)

for i, a in enumerate(A):
    ans[a] = i+1
ans.pop(0)


print(*ans)
