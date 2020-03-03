import numpy as np
import copy as cp

# 参考: https://qiita.com/snow67675476/items/e87ddb9285e27ea555f8
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append(i)

    if temp!=1:
        arr.append(temp)

    if arr==[]:
        arr.append(n)

    return arr


A, B = map(int, input().split())

ans = [1]

for a in factorization(A):
    for b in factorization(B):
        if a == b:
            ans.append(a)

print(len(ans))
