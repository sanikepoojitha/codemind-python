a=int(input())
b=input()
arr=list(b.split())
mi=0
for i in arr:
    if len(i)>mi:
        mi=len(i)
c=0
for i in arr:
    if len(i)==mi:
        print(i,end=" ")