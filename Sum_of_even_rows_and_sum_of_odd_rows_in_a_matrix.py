x,y=map(int,input().split())
c,c1=0,0
for i in range(x):
    a=list(map(int,input().split()))
    d=sum(a)
    if(i%2==0):
        c+=d
    else:
        c1+=d
print(c,c1)