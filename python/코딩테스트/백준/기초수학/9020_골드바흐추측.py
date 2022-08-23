import sys
t=int(sys.stdin.readline())
a=0
while a<t:
    n=int(sys.stdin.readline())
    pn=[True for i in range(n+1)]
    pn[0]=False
    pn[1]=False
    p=2
    while p*p<=n:
        if pn[p]:
            for i in range(p*p,n+1,p):
                pn[i]=False
        p+=1
    cn=[]
    for i in range(n+1):
        if pn[i]:
            cn.append(i)
    for i in cn:
        if n-i<=i and pn[i] and i in cn and n-i in cn:
            print(n-i,i)
            break
            
    a+=1