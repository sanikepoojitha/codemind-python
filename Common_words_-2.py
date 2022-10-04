l=list(map(str,input().split()))
ll=list(map(str,input().split()))
b=[]
c=[]
for i in ll:
    if ll.count(i)>1:
        b.append(i)
for i in l:
    if l.count(i)>1:
        c.append(i)
for i in range(len(l)):
    l[i]=l[i].lower()
for i in range(len(ll)):
    ll[i]=ll[i].lower()
a=[]
for i in l:
    for j in ll:
        if i==j and i!=' ':
            if i not in a and i not in b and i not in c:
                a.append(i)
print(len(a))