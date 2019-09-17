import sys
import numpy as np
import math
import heapq
def input():
    return sys.stdin.readline()[:-1]

N, M = map(int, input().split())
A = list(map(lambda a: int(a)*(-1), input().split()))
heapq.heapify(A)

for _ in range(M):
    heapq.heappush(A, math.trunc(heapq.heappop(A) / 2))

print(sum(A)*(-1))
