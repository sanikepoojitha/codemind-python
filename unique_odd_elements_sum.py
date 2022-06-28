n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(n):
    c=0
    for j in range(i,n):
        if l[i]==l[j]:
            c+=1
    if c==1:
        if l[i]%2==1:
            s+=l[i]
        
print(s) 