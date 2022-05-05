n=int(input())
r=0
sum=0
sq=n*n
while sq>0:
    r=sq%10
    sum+=r
    sq=sq//10
if sum==n:
    print('Neon Number')
else:
    print('Not Neon Number')