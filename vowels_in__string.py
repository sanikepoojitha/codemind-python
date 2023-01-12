s="AEIOUaeiou"
n=input()
ss=[]
for i in n:
    if i in s:
        if i not in ss:
            ss.append(i)
print(*ss)