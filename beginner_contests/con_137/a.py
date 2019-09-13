A, B = map(int, input().split())

answers = [A+B, A-B, A*B]
print(max(answers))