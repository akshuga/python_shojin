import bisect

n=1000   # 1<=n<=1000
m=10000
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
kk=[]
for i in k:
    for j in k:
        kk+=[i+j]
kk=sorted(kk)
f=False
for a in k:
    for b in k:
        cd = m-a-b
        idx = bisect.bisect(kk,cd)
        if kk[idx-1]==cd:
            # print(a+b,cd)
            f=True

if f:
    print('Yes')
else:
    print('No')