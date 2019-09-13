import numpy as np

K, X = map(int, input().split(' '))

max_num = X + K

min_num = X - K + 1

print(*np.arange(min_num, max_num))
