""" import sys
n,m= list(map(int,sys.stdin.readline().split()))
if n==1 :
    n=2
lst= [1 for i in range(n,m+1)]
for j in range(2,m+1):
    for k in range(m-n+1):
        if (k+n)%j==0 and (k+n) != j:
            lst[k]=0
for c in range(len(lst)):
    if lst[c]==1:
        sys.stdout.write()(c+n) """
import sys
n,m= list(map(int,sys.stdin.readline().split()))
pn = [True for i in range(m+1)]
pn[0]= False
pn[1]= False
p = 2
while (p*p <= m):
    if (pn[p]):
        for i in range(p*p, m+1, p):
            pn[i] = False
    p += 1
for i in range(n,m+1):
    if (pn[i]):
        print(i)