n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    if l[i]<0:
        l[i]=-1*l[i]
l=sorted(l)
for i in range(n):
    l[i]=l[i]**2
print(*l)