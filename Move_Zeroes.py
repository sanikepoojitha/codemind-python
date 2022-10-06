n=int(input())
l=list(map(int,input().split()))
c=l.count(0)
a=[]
for i in range(n):
    if l[i]!=0:
        a.append(l[i])
for i in range(c):
    a.append(0)
print(*a)