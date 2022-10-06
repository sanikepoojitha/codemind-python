n=int(input())
l=list(map(int,input().split()))
ll=list(set(l))
max=0
m=0
for i in range(len(ll)):
    c=0
    for j in range(n):
        if ll[i]==l[j]:
            c+=1
    if c>max:
        max=c
        m=ll[i]
print(m)