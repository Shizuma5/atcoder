import math
import sys
import numpy as np

def input():
    return sys.stdin.readline()[:-1]

N, K = map(int, input().split())
h = np.array(list(map(int, input().split())))

print(np.sum(h >= K))
