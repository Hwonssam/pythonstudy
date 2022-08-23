n=int(input())
s=n-len(str(n))*9
if s <1:
    s=1
ss=0
for i in range(s,n+1):
    ans=i
    for j in range(len(str(i))):
        ans+=int(str(i)[j])
    if ans==n:
        ss=i
        break
print(ss)
