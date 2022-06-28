n=int(input())
f=0
s=0
t=0
for i in range(1,n+1):
    if n%i==0:
        f+=1
if f==2:
    w=n
    while(w!=0):
        r=w%10
        s=s*10+r
        w=w//10
    for i in range(1,s+1):
        if s%i==0:
           t+=1
    if t==2:
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")