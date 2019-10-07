import sys

def input():
    return sys.stdin.readline()[:-1]

N, A, B = map(int, input().split())

taxi = N * A
train = B

if taxi > train:
    print(train)
else:
    print(taxi)

