N, Q = map(int, input().split(' '))

# アルファベットの文字列配列を作成（N子分）
alpha = ''
for s in range(65, 65+N):
    alpha += chr(s)

# 前後の文字列を比較するためのパイプ
pipe = 1
# 次に入れ替えをスタートする位置
first_pipe = 1
# ループを抜けるための変数
is_end = True
# ループ用変数
i = 0

while Q > i:
    print("? {} {}".format(alpha[pipe-1], alpha[pipe]))
    # queryを受け取る
    query = input()
    if query == '<':
        pipe += 1
    else: # >
        alpha = alpha[:pipe-1] + alpha[pipe] + alpha[pipe-1] + alpha[pipe+1:]
        if is_end:
            first_pipe = pipe - 1
        pipe += 1

        # ソートがまだ未完の可能性があるのでFalseに
        is_end = False

    if pipe == N:
        # is_endがTrueだとループを抜ける
        if is_end:
            break
        else:
            # パイプの初期化
            if first_pipe == 0:
                pipe = 1
            else:
                pipe = first_pipe
            # Trueのままだとソート完了
            is_end = True
            continue
    i += 1

print("! {}".format(alpha))