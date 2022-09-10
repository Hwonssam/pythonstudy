import sys
n,m=list(map(int,input().split()))
n_lst=[input() for i in range(n)]
m_lst=[input() for i in range(m)]


n_lst.sort()
def bi(array,search):
    l=0
    r=n-1
    while l<=r:
        mid=(l+r)//2
        a=sorted([array[mid],search])
        if array[mid] == search:
            return 1
        elif a[0]==search:
            r=mid-1
        else :
           l=mid+1
    return 0

cnt=0
for i in m_lst:
    cnt += bi(n_lst,i)
print(cnt)

""" 다른사람풀이1
pr = open(0).read().split('\n')
N, M = map(int, pr[0].split())
S = set()
for i in range(1,N+1):
    S.add(pr[i])
cnt = 0
for j in range(M):
    if pr[N+1+j] in S: cnt+=1
print(cnt) 

풀이2
import sys

N, M = map(int, sys.stdin.readline().strip().split())
str = sys.stdin.read().split()
S, command = set(str[:N]), str[N:]
print(sum(1 for i in command if i in S))"""