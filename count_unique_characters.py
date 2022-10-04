n=input()
n=n.lower()
s=0
for i in n:
    c=0
    for j in n:
        if i==j and i!=' ':
            c+=1
    if c==1:
        s+=1
print(s)