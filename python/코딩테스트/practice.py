n,m=list(map(int,input().split()))
f=0
a=[]
while f<n:
    u=input()
    a.append(u)
    f+=1
for i in range(n):
    ab=[]
    for j in range(m):
        if a[i][j]=='W':
           ab.append(True)
        else:
           ab.append(False)
    a[i]=list(ab)

w_right=[]
b_right=[]
cnt=1
for i in range(8):
    lst=[]
    cnt+=1
    for i in range(8):
        if cnt%2==0:
            lst.append(True)
        else :
            lst.append(False)
        cnt+=1
    w_right.append(list(lst))
for i in range(8):
    lst=[]
    cnt+=1
    for i in range(8):
        if cnt%2==1:
            lst.append(True)
        else :
            lst.append(False)
        cnt+=1
    b_right.append(list(lst))
def check(t):
    cnt2=0
    cnt3=0
    for i in range(8):
        for j in range(8):
            if t[i][j]!=w_right[i][j]:
                cnt2+=1
            if t[i][j]!=b_right[i][j]:
                cnt3+=1
    if cnt2<=cnt3:
        ans=cnt2
    else:
        ans=cnt3
    return ans
t=list(a)
c=2500
for i in range(n-7):
    t=a[i:i+8]
    for j in range(m-7):
        for k in range(8):
            t[k]=a[k][j:j+8]
        if c>check(t):
            c= check(t)
print(c)