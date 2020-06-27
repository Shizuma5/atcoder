# 累積和
- 配列の区間内の和を求められる際に、事前計算をしておくことで計算量を減らす
```
[a0, a1, a2, a3, a4]の時に
s1 = a0
s2 = a0 + a1
s3 = a0 + a1 + a2
...
をsとすると
s5 - s2をするだけで、O(1)で3~5の区間の累積和を得られる
```
- https://qiita.com/drken/items/56a6b68edef8fc605821

# 等差数列の和
- 初項1, 交差1の等差数列の和は
    - 1 + 2 + 3 + ... X = X(X+1)/2
- 数列に気づくのは難しいかもしれないけど頭に入れておこう