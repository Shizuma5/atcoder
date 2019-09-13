# dfs(深さ優先探索)
# d問題AC

N, Q = map(int, input().split(' '))

num_list = [0] * (N+1)

tree_list = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    tree_list[a].append(b)
    tree_list[b].append(a)

for _ in range(Q):
    p, x = map(int, input().split())
    num_list[p] += x

q = [1]
checked = [0] * (N+1)

while q:
    v=q.pop()
    checked[v] = 1
    for u in tree_list[v]:
        if checked[u] == 1:
            continue
        num_list[u] += num_list[v]
        q.append(u)

print(*num_list[1:])