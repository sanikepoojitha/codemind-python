n=int(input())
l=list(map(int,input().split()))
j=n-1
s=0
for i in range(n):
    if j>=0:
        s=s+(l[i]*(2**j))
        j-=1
print(s)