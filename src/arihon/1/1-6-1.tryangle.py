n=5
a=[2,3,4,5,10]

# n=4
# a=[4,5,10,20]

# 3つの棒x<=y<=zで三角形が作れる
# i.e. z(max) < x+y

# n=100
# -> n^3=10^6 なので間に合いそう

ans=0

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            # print(i,j,k)
            lst = [a[i],a[j],a[k]]
            # print(lst)
            m = max(lst) # z
            length = sum(lst)
            rest = length-m # x+y
            if m<rest:
                ans=max(ans,length)

print(ans)
