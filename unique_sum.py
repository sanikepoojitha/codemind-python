n=int(input())
l=list(map(int,input().split()))
l=set(l)
c=0
l=list(l)
for i in l:
    c+=i
print(c)