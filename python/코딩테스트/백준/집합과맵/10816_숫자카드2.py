import sys
pr=open('input.txt','r').read().rstrip().split('\n')
n=int(pr[0])
n_lst=map(int,pr[1].split())
m=int(pr[2])
m_lst=list(map(int,pr[3].split()))
cnt_lst=[0]*20000001
for i in n_lst:
    cnt_lst[i+10000000] +=1
print(' '.join(map(lambda x :str(cnt_lst[x+10000000]),m_lst)))
""" 
import sys
stdin = sys.stdin.read().splitlines()
A = map(int,stdin[1].split())
B = map(int,stdin[3].split())
dic = {}
for n in A:
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1
print(' '.join(str(dic[n]) if n in dic else '0' for n in B)) """