n=input()
aa=ee=ii=oo=uu=0
for p in n:
    if p=='a':
        aa+=1
    elif p=='e':
        ee+=1
    elif p=='o':
        oo+=1
    elif p=='i':
        ii+=1
    elif p=='u':
        uu+=1
if aa==0 or ee==0 or ii==0 or oo==0 or uu==0:
    print("False")
else:
    print("True")