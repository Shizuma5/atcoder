import sys
def input():
    return sys.stdin.readline()[:-1]

def is_match(S, I):
    num = len(S) - len(I)
    I_2 = []
    if num > 0:
        I_2 = ['0'] * (num)
        I_2.extend(I)
    else:
        I_2 = I
    for s, i in zip(S, I_2):
        if s == i or s == '?':
            continue
        else:
            return False
    return True

S = list(input())

denominator = 10 ** 9 + 7

answer = 0

i = 5
while i < 10 ** len(S):
    if is_match(S, list(str(i))):
        answer += 1
    i += 13

print(answer % denominator)
