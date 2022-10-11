n=int(input())
l=list(map(int,input().split()))
h=0
mi=l.index(min(l))
ma=l.index(max(l))
if mi<ma:
    for i in range(mi,ma+1):
        c=0
        for j in range(1,l[i]+1):
            if l[i]%j==0:
                c+=1
        if c==2:
            h+=1
else:
    for i in range(ma,mi+1):
        c=0
        for j in range(1,l[i]+1):
            if l[i]%j==0:
                c+=1
        if c==2:
            h+=1
print(h)