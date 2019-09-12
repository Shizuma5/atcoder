N, Q = map(int, input().split(' '))

num_list = [0] * (N+1)
tree_list = [[i] for i in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split(' '))
    for i, t in enumerate(tree_list):
        if i == 0:
            continue
        if a in t:
            tree_list[i].append(b)

for _ in range(Q):
    p, x = map(int, input().split(' '))
    for num in tree_list[p]:
        num_list[num] += x

num_list.pop(0)
print(*num_list)
