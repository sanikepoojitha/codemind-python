n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(n):
    s=0
    while(l[i]!=0):
        r=l[i]%10
        s=s*10+r
        l[i]=l[i]//10
    a.append(s)
print(*a)