n=3
m=10
k=[1,3,5]

f=False
for a in k:
    for b in k:
        for c in k:
            for d in k:
                if(a+b+c+d==m):
                    f=True

if f:
    print('Yes')
else:
    print('No')