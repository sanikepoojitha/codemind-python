l=list(map(str,input().split()))
for i in range(len(l)):
    if i%2==0:
        l[i]=l[i][::-1]
print(*l)