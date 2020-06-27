N, M, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 経過時間
t = 0
# 読んだ本
book_count = 0

while t <= K:
    if len(A) == 0 and len(B) == 0:
        break
    elif len(A) == 0:
        t += B.pop(0)
        if t <= K:
            book_count += 1
    elif len(B) == 0:
        t += A.pop(0)
        if t <= K:
            book_count += 1
    else:
        if A[0] < B[0]:
            t += A.pop(0)
            if t <= K:
                book_count += 1
        else:
            t += B.pop(0)
            if t <= K:
                book_count += 1

print(book_count)
