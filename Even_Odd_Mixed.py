x=int(input())
c=0
c2=0
c1=0
while x>0:
    r=x%10
    if(r%2==0):
        c+=1
    else:
        c1+=1
    c2+=1
    x=x//10
if c==c2:
    print('Even')
elif c1==c2:
    print('Odd')
else:
    print('Mixed')