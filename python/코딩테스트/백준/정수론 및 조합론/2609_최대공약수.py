a=list(map(int,input().split()))
lst=[]
div=2
while div<=a[0]+1 and div <=a[1]+1: 
    if a[0]%div==0 and a[1]%div ==0:
        a[0]=int(a[0]/div)
        a[1]=int(a[1]/div)
        lst.append(div)
        div=1
    div+=1
v=1
if lst != [] :
    for i in lst :
        v=v*i
print(v)
if a[0] != a[1]:
    for i in a:
        v=v*i
else :
    v=v*a[0]
print(v)