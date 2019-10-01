import sys
def input():
    return sys.stdin.readline()[:-1]

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B.append(0)

monster_count = 0
next_saver = 0

for i in range(N+1):
    if A[i] > B[i] + next_saver:
        monster_count += B[i] + next_saver
        next_saver = 0
    else:
        monster_count += A[i]
        if A[i] <= next_saver:
            next_saver = B[i]
        else:
            next_saver = B[i] - (A[i]-next_saver)
print(monster_count)
