x=int (input())
a=list(map(int,input().split()))
for i in range(0,x):
    c=0
    d=a[i]
    for j in range(0,x):
        if d>a[j] and i!=j:
            c=c+1
    print(c,end=" ")    