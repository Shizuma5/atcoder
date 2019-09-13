N, M = map(int, input().split())

reword = [0] * M

for _ in range(N):
    A, B = map(int, input().split())
    deadline = -1 * A
    if reword[deadline] > 0:
        i = 0
        while abs(deadline) < M:
            if reword[deadline] > B:
                reword[deadline] = B
            else:
                for 
    else:
        reword[deadline] = B