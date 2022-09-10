pr=open(0).read().rstrip().split('\n')
n=int(pr[0])
n_lst=map(int,pr[1].split())
m=int(pr[2])
m_lst=map(int,pr[3].split())
cnt_lst=[0]*m
dic=dict(zip(m_lst,range(m)))
for i in n_lst:
    try:
        cnt_lst[dic[i]] +=1
    except:
        continue
print(' '.join(map(str,cnt_lst)))