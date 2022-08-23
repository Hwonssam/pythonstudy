t=int(input())
a=0
lst=[]
while a < t:
    n= int(input())
    lst.append(n)
    a+=1
lst.sort()
for i in lst:
    print(i)