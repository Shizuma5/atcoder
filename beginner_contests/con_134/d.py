# https://note.mu/tanon_cp/n/nf77205916310

import sys
def input():
    return sys.stdin.readline()[:-1]

N = int(input())
A = list(map(int, input().split()))

flag=[-1]*N #0～n-1番目の箱にボールを入れたかどうかの情報を入れる
ans=[]
for i in range(N-1,-1,-1):
    cnt=0
    for j in range(i,N,i+1): #i番目以降のiの倍数の箱にボールが何個入っているかを数える
        if j==i:
            continue
        else:
            if flag[j]==1:
                cnt+=1
    if (A[i]+cnt)%2==0: #箱にボールを入れるかの判定
        flag[i]=0
    else:
        flag[i]=1
        ans.append(i+1) #ボールを入れた箱のインデックスを答えに追加
num=len(ans)
if num==0: #ボールを入れた箱がなければ答えは0
    print(0)
else: #ボールを入れた箱があれば入れた箱の数とそのインデックスを出力
    print(num)
    print(*ans)
