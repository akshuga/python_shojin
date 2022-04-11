import bisect

n=100   # 1<=n<=1000
m=1000
k=list(range(1,n*3+1,3))
# print(k)
# print(len(k))

# 4重ループは10^12となって間に合わない

# 一番内側のループ
# a+b+c+d=mとなるdを見つける
# d=m-(a+b+c)となるdを見つける

# 二分探索 binary search
# リストはソート済みとする

k=sorted(k)
f=False
for a in k:
    for b in k:
        for c in k:
            d = m-a-b-c
            idx = bisect.bisect(k,d)
            if k[idx-1]==d:
                # print(a+b+c,d)
                f=True

if f:
    print('Yes')
else:
    print('No')