x,y=map(int,input().split())
c=0
for i in range(x):
    a=list(map(int,input().split()))
    d=sum(a)
    if(c<d):
        c=d
print(c)