import math
import sys

def input():
    return sys.stdin.readline()[:-1]

N = int(input())

odd = math.ceil(N / 2)

print(odd / N)
