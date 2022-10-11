import math
 
a,b,c,d = map(int,input().split())
 
def isPrime(n):
  if n == 2:
    return True
  if n % 2 == 0:
    return False
  m = math.floor(math.sqrt(n)) + 1
  for p in range(3, m, 2):
      if n % p == 0:
        return False
  return True
 
for i in range(a,b+1):
    t = 0
    for j in range(c,d+1):
        flag = isPrime(i+j) 
        if(flag == False):
              t += 1
        if t == d - c + 1:
              print("Takahashi")
              break
    if(t == d - c + 1):
        break
else:
    print("Aoki")