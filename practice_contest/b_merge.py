N, Q = map(int, input().split(' '))

# アルファベットの文字列配列を作成（N子分）
alpha = ''
for s in range(65, 65+N):
    alpha += chr(s)

def merge_sort(string):
    if len(string) <= 1:
        return string
    # 小数点以下切り捨て
    middle = len(string) // 2

    left = string[:middle]
    right = string[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    merged_str = ''
    l_i, r_i = 0, 0

    while l_i < len(left) and r_i < len(right):
        print("? {} {}".format(left[l_i], right[r_i]))
        query = input()
        # 左の最小と右の最小を比較して小さい方からマージしていく
        if query == '<':
            merged_str += left[l_i]
            l_i += 1
        else:
            merged_str += right[r_i]
            r_i += 1
    if l_i < len(left):
        merged_str += left[l_i:]
    if r_i < len(right):
        merged_str += right[r_i:]
    return merged_str

alpha = merge_sort(alpha)

print("! {}".format(alpha))