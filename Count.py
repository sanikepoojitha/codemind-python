x=int(input())
c=0
c1=0
a=list(map(int,input().split()))
for i in range(0,x):
    if a[i]%2==0:
        c=c+1
    else:
        c1=c1+1
print(c,c1)        