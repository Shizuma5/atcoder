import numpy as np

def distance(x1, x2):
    return np.sqrt((x1[0] - x2[0])**2 + (x1[1] - x2[1])**2)

N = int(input())
X = []

N_exs = [0, 1, 2, 6, 24, 120, 720, 5040, 40320]

for _ in range(N):
    A, B = map(int, input().split())
    X.append([A, B])

total = 0
for i in range(N):
    for j in range(N-1, i, -1):
        if i == j:
            continue
        total += distance(X[i], X[j])

num = int((N * N - N) / 2)

# 1パターンあたりにN-1個ルートがあり、どのルートも均等に存在する
ans = total * (N-1) / num

print(ans)
