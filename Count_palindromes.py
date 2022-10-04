n=int(input())
l=list(map(int,input().split()))
b=[]
for i in range(n):
    b.append(l[i])
c=0
for i in range(n):
    s=0
    while b[i]!=0:
        r=b[i]%10
        s=s*10+r
        b[i]=b[i]//10
    if s==l[i]:
        c+=1
print(c)