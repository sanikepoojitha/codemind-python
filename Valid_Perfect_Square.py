n=int(input())
import math
for i in range(1,n+1):
    a=int(input())
    s=math.sqrt(a)
    y=s-math.floor(s)
    if y==0:
        print('True')
    else:
        print('False')
    s=0    
    