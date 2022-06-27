n=int(input())
l=list(map(int,input().split()))
m=[]
w=0
for i in range(n):
    c=0
    for j in range(n):
        if l[i]==l[j]:
            c+=1
    if c==l[i]:
        w+=1
        m.append(l[i])
        l[i]=0
if w==0:
    print('-1')
else:
    print(*m)