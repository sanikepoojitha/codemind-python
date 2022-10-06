n,k=map(int,input().split())
s=c=0
l=list(map(int,input().split()))
for i in range(n):
    if l[i]>k and s>0:
        break
    if l[i]>k:
        s=1
    else:
        c+=1
print(c)    