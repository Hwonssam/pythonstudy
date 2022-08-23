import math 
a,b,c=list(map(int,input().split()))
if b < c :
    print(math.floor(a/(c-b)+1))
elif b >=c:
    print('-1')
