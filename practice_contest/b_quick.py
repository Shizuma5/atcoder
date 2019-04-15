N, Q = map(int, input().split(' '))

# アルファベットの文字列配列を作成（N子分）
alpha = ''
for s in range(65, 65+N):
    alpha += chr(s)

def quick_sort(string):
    left = ''
    right = ''
    if len(string) <= 1:
        return string
    
    piv = string[0]

    for alpha in string:
        if piv == alpha:
            continue
        print("? {} {}".format(piv, alpha))
        query = input()
        if query == '<':
            right += alpha
        elif query == '>':
            left += alpha
    # 再起で左右をソート
    left = quick_sort(left)
    right = quick_sort(right)
    return left + piv + right

alpha = quick_sort(alpha)

print("! {}".format(alpha))