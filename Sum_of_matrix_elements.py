r=int(input())
c=int(input())
s=0
for i in range(r):
    l=list(map(int,input().split()))
    for j in range(c):
        s+=l[j]
print(s)