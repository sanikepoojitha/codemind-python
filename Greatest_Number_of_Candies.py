x=int(input())
a=list(map(int,input().split()))
y=int(input())
for i in a:
    if i+y>=max(a):
         print("True",end=" ")
    else:
         print(False,end=' ')