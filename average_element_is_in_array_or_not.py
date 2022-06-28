n=int(input())
l=list(map(int,input().split()))
s=0
c=0
for i in range(n):
    s+=l[i]
a=s//n
for i in range(n):
    if l[i]==a:
        c+=1
if c==0:
    print("False")
else:
    print("True")