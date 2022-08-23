a=int(input())
if a ==1:
    a = 2
b=int(input())
c=list(range(a,b+1))
for i in range(2,b+1):
    for j in c :
        try:
            if j != i and j%i==0 :
                c.remove(j)
        except :
            pass
d = sum(c)
if c == [] :
    print('-1')
else :
    print(d)
    print(c[0])