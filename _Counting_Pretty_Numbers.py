x=int(input())
r=0
c=0
for i in range(1,x+1):
    a,b=map(int,input().split())
    for j in range(a,b+1):
        r=j%10
        if r==2 or r==3 or r==9:
            c=c+1
    print(c)
    c=0