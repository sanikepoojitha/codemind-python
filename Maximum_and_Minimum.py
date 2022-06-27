n=int(input())
l=list(map(int,input().split()))
min=99999999
max=0
g=0
for i in range(n):
    c=0
    for j in range(n):
        if l[i]==l[j]:
            c+=1
    if c==l[i]:
        if l[i]>max:
            max=l[i]
        if l[i]<min:
            min=l[i]
        g+=1
if g==0:
    print('-1')
else:
    print(min,max)