x=int(input())
y=int(input())
sum=x+y
c=0
d=0
i=sum
while True:
    i=i+1
    c=c+1
    d=0
    for j in range(1,i+1):
        if i%j==0:
            d+=1
    if d==2:
        break
print(c)    