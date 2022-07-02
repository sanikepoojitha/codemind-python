x=input()
n="0123456789"
a=[]
for i in x:
    if i in n:
        a.append(int(i))
print(sum(a))