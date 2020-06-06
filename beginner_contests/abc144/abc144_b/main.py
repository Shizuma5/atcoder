N = int(input())

match_list = list(set([i * j for i in range(1, 10) for j in range(1, 10)]))

if N in match_list:
    print('Yes')
else:
    print('No')
