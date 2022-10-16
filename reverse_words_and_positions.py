l=list(map(str,input().split()))
ll=l[::-1]
for i in range(len(ll)):
    ll[i]=ll[i][::-1]
print(*ll)