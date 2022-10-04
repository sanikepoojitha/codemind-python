n=list(map(str,input().split()))
l=len(n)
m=min(n[l-1])
nn=m.lower()
c=0
for i in n[len(n)-1]:
    if nn==i:
        c=1
        break
if c==1:
    print(nn)
else:
    print(m)