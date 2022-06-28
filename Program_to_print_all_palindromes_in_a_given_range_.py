x=int(input())
y=int(input())
for i in range(x,y):
    a=i
    sum=0
    while i>0:
        r=i%10
        sum=sum*10+r
        i=i//10
    if sum==a:
        print(a,end=" ")