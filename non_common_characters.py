a=input()
a=a.lower()
b=input()
b=b.lower()
s=[]
for i in a:
    if i not in  b:
        if i not in s:
            if i!=' ':
                s.append(i)
for i in b:
    if i not in a:
        if i not in s:
            if i!=' ':
                s.append(i)
s=sorted(s)
for i in (s):
    print(i,end='')