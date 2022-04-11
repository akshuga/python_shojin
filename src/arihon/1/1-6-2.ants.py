L=10
n=3
x=[2,6,7]

# L=21
# n=6
# x=[4,9,11,13,17,19]


# 最小
# すべてのアリが近い方の端に向かう

# 最大
# アリがぶつかる、を
# アリがすれ違う、としても問題は変わらない
# -> n匹それぞれの端までの距離の最大値

#「 発想力が問われる問題」

# n匹を一度ずつ調べるだけ O(n)
# n=10^6でも間に合いそう


min_time=0
for i in range(n):
    min_time=max(min_time,min(x[i],L-x[i]))
    # print(min_time)

max_time=0
for i in range(n):
    max_time=max(max_time,max(x[i],L-x[i]))
    # print(max_time)

print(min_time,max_time)
