x=int(input())
a=list(map(int,input().split()))
y=int(input())
c=0
for i in range(0,x):
    if y==a[i]:
        print(i,end=" ")
        c=c+1
        break
for i in range(x-1,-1,-1):
    if y==a[i]:
        print(i)
        c=c+1
        break
if c!=2:
    print('-1 -1')
        