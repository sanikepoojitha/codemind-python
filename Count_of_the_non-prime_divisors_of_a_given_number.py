x=int(input())
c=0
c1=0
for i in range(1,x+1):
    if x%i==0:
        for j in range(1,i+1):
            if i%j==0:
                c=c+1
        if c!=2:
            c1=c1+1
    c=0
print(c1)    