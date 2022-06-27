n=int(input())
l=list(map(int,input().split()))
s=0
m=0
for i in range(n):
    c=0
    for j in range(n):
        if l[i]==l[j]:
            c+=1
    if c==l[i]:
        s=s+l[i]
        m+=1
        l[i]=0
if m==0:
    print('-1')
else:
    print("%.2f"%(s/m))