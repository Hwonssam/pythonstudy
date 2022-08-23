lst=[1,1,2,2,2,8]
n=list(map(int,input().split()))
ans=[]
for i in range(len(lst)):
    ans.append(str(lst[i]-n[i]))
print(' '.join(ans))