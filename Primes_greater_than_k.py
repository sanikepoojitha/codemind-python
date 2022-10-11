n=int(input())
l=list(map(int,input().split()))
k=int(input())
c=0
for i in range(n):
    m=0
    for j in range(1,l[i]+1):
        if l[i]%j==0:
            m+=1
    if m==2:
        if l[i]>=k:
            c+=1
print(c)