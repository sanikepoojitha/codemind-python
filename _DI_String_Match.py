a=input()
I=0
D=len(a)
for i in a:
    if i=='I':
        print(I,end=' ')
        I+=1
    if i=='D':
        print(D,end=' ')
        D-=1
if a[len(a)-1]=='I':
    print(I)
else:
    print(D)