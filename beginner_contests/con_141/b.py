import sys

S = input()

for i, letter in enumerate(list(S)):
    if letter == 'U' or letter == 'D':
        continue
    
    if ((i+1) % 2 == 0 and letter == 'R') or ((i+1) % 2 == 1 and letter == 'L'):
        print('No')
        sys.exit()
print('Yes')