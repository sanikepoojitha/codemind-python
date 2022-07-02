def rev(s):
    s1=""
    l=len(s)
    for i in range (l-1,-1,-1):
        s1+=s[i]
    return s1
a=input()
print(rev(a))