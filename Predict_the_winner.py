n=int(input())
l=list(map(int,input().split()))
h=n//2
if n%2==1:
    h+=1
s=0
s1=0
for i in range(h):
    s+=l[i]
for i in range(h,n):
    s1+=l[i]
tot=abs(s-s1)
if tot%4==0:
    print("X")
else:
    print("Y")