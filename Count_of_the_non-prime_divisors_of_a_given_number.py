n=int(input())

c=0
for i in range(1,n):
    if n%i==0:
        f=0
        for j in range(1,i+1):
            if i%j==0:
                f+=1
        if f!=2:
            c+=1
print(c+1)