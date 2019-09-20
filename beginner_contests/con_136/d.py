import sys
def input():
    return sys.stdin.readline()[:-1]

S = list(input())
S.append('R')

ans = []

R_count = 0
L_count = 0
before = 'R'

for R_L in S:
    if before == 'L' and R_L == 'R':
        ans.extend([0]*(R_count-1))
        total = R_count + L_count
        if total % 2 == 0:
            ans.extend([int(total/2), int(total/2)])
        elif total % 2 == 1:
            if R_count % 2 == 1:
                ans.extend([int(total/2) + 1, int(total/2)])
            else:
                ans.extend([int(total/2), int(total/2) + 1])
        ans.extend([0]*(L_count-1))
        R_count = 0
        L_count = 0
    if R_L == 'R':
        R_count += 1
        before = 'R'
    elif R_L == 'L':
        L_count += 1
        before = 'L'

print(*ans)