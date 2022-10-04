l=list(map(str,input().split()))
a=[]
for i in l:
    a.append(min(i))
    a.append(max(i))
print(*a)