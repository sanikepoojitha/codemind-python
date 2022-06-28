x=int(input())
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    if(x>a or x>b):
        print('UPLOAD ANOTHER')
    else:
        if(a==b):
            print('ACCEPTED')
        else:
            print('CROP IT')