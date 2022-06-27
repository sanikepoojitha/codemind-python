n=int(input())
l=list(map(int,input().split()))
m=int(input())
f=0
mm=[]
for i in range(n):
    c=0
    for j in range(n):
        if l[i]==l[j]:
            c+=1
    if c==m:
        f+=1
        mm.append(l[i])
        l[i]=0
if f==0:
    print('-1')
else:
    print(*mm)