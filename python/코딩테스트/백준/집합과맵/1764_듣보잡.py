def bi(array,search):
    l=0
    r=len(array)-1
    while l<=r:
        mid=(l+r)//2
        a=sorted([array[mid],search])
        if array[mid] == search:
            return mid
        elif a[0]==search:
            r=mid-1
        else :
           l=mid+1
pr=open('input.txt','r').read().split('\n')
n,m=map(int,pr[0].split())
lis=sorted(pr[1:n+1])
see=pr[n+1:]
answer=[]
for i in see:
    c=bi(lis,i)
    if c != None:
        answer.append(c)
answer.sort()
print(len(answer))
print('\n'.join(lis[i] for i in answer))
""" 
import sys
n, m = map(int, input().split())
nameList = sys.stdin.read().splitlines()
hearset = set(nameList[:n])
seeset = set(nameList[n:])
ret = list(hearset & seeset)
ret.sort()
print(len(ret))
for i in ret:
    print(i) """

