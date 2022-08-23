t=input()
a=list(map(int,input().split()))
a=sorted(a)
c=list(range(2,(a[-1])+1))
for i in range(2,(a[-1]+1)):
    for j in c :
        try:
            if j != i and j%i==0 :
                c.remove(j)
        except :
            pass
cnt = 0
for d in a :
    if d in c :
        cnt +=1
print(cnt)
