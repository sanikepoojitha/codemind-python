n=int(input())
l=list(map(int,input().split()))
k=n//2
a=[]
b=[]
c=[]
if n%2==1:
    for i in range(k+1):
        a.append(l[i])
    for i in range(n-1,k,-1):
        b.append(l[i])
    b.append(0)
    for i in range(k+1):
        c.append(a[i])
        c.append(b[i])
else:
    for i in range(k):
        a.append(l[i])
    for i in range(n-1,k-1,-1):
        b.append(l[i])
    for i in range(k):
        c.append(a[i])
        c.append(b[i])

print(*c)