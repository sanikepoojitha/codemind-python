a=list(map(int,input().replace(',',' ').split()))
d=[]
k=0
for i in a:
    b=[]
    for j in range(1,i+1):
        if(i%j==0):
            b.append(j)
    c=sum(b)
    if c in a:
        d.append(i)
        k=1
if(k==0):
    print('-1')
else:
    print(*sorted(d))