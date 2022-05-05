x=int(input())
sum=0
for i in range(1,x+1):
    a=int(input())
    d=a
    while a>0:
        r=a%10
        sum=sum*10+r
        a=a//10
    if sum==d:
        print('True')
    else:
        print('False')
    sum=0    
        