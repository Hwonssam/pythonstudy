def prince(array):
    x1,y1,x2,y2=map(int,array[0].split())
    b=int(array[1])
    cnt=0
    for i in array[2:2+b]:
        c1,c2,r=map(int,i.split())
        if (x1-c1)**2+(y1-c2)**2<=r*r or (x2-c1)**2+(y2-c2)**2<=r*r:
            cnt+=1
        if (x1-c1)**2+(y1-c2)**2<=r*r and (x2-c1)**2+(y2-c2)**2<=r*r:
            cnt-=1
    print(cnt)
    return b
pr=open('input.txt','r').read().split('\n')
t=int(pr[0])
a=0
for i in range(t):
    array=pr[a+1:]
    a+=prince(array)+2

