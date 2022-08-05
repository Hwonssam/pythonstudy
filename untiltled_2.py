import math
answer = []
n=4
lst=[]
n2 =sum(range(1,n+1))
for i in range(1,n2+1):
    lst.append(i)
lst.reverse()
lst2 =[[0]*i for i in range(1,n+1)]
print(lst2)
for i in lst :
    for j in range(0,n) :
        for c in range(0,n):
            try:
                if lst2[j][c] == 0 :
                    lst2[j][c]=i
            except :
                break
print(lst2)


