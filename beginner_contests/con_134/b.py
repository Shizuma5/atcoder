import math
import sys
def input():
    return sys.stdin.readline()[:-1]

N, D = map(int, input().split())

watch_range = D * 2 + 1

print(math.ceil(N / watch_range))
