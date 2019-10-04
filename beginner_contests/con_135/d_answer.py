import pprint as pp

s=input()
l=len(s)
mod=10**9+7
dp=[[0 for j in range(13)] for i in range(l+1)]
dp[0][0]=1 #初期値の設定
pp.pprint(dp)
for i in range(l):
    if s[i]=='?': #?のときは各値(0～9)について更新する
        for j in range(10):
            for k in range(13):
                dp[i+1][(k*10+j)%13]+=dp[i][k]%mod
    else:
        for k in range(13): #整数のときはその値について更新する
            dp[i+1][(k*10+int(s[i]))%13]+=dp[i][k]%mod
    pp.pprint(dp)
print(dp[-1][5]%mod) #最後まで更新を行ったときのあまりが5となる数の個数が答え
