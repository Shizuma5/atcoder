from scipy.special import comb

X, Y = map(int, input().split())

# 足した時の値が3の倍数でない時は除去
if not (X+Y) % 3 == 0:
    print(0)

# min / max が1/2以下の時も除去
elif min([X,Y]) / max([X, Y]) < 0.5:
    print(0)

else:
    move_count = 0
    diff = abs(int(Y - X))
    num_3_3 = int(int(X - diff) / 3)

    move_count = diff + num_3_3 * 2

    ans = comb(move_count, num_3_3+diff, exact=True)

    print(ans)
