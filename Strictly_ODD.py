n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    if l[i]%2==1:
        if i%2!=1:
            c+=1
            break
if c==0:
    print("True")
else:
    print("False")