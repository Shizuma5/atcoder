N = int(input())
S = input()

if N % 2 == 1:
    print('No')
else:
    N = int(N / 2)
    T1 = S[:N]
    T2 = S[N:]
    if T1 == T2:
        print('Yes')
    else:
        print('No')
