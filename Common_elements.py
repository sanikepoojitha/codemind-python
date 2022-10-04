n,m=map(int,input().split())
l=list(map(int,input().split()))
ll=list(map(int,input().split()))
a=[]
for i in l:
    if i in ll:
        if i not in a:
            a.append(i)
print(*a)