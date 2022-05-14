x=int(input())
a=list(map(int,input().split()))
for i in range(x-1,(x//2)-1,-1):
    print(a[i],end=" ")
for i in range(0,x//2):
    print(a[i],end=" ")
    