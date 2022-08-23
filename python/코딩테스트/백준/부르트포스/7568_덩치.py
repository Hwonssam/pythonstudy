#t=int(input())
""" t=5
n=0
x_lst=[]
y_lst=[]
k=[] """
""" while n<t:
    x,y=list(map(int,input().split()))
    x_lst.append(x)
    y_lst.append(y) 
    n+=1"""
""" x_lst=[55,58,88,60,46]
y_lst=[185,183,186,175,155]
for i in range(t):
    cnt=0
    for j in range(t):
        if x_lst[i]>x_lst[j] and y_lst[i]>y_lst[j]:
            cnt+=1
    k.append(cnt)
print(k)
k2=sorted(k,reverse=True)
k3=list(k2)
d=1
k_ans=list(k)
for i in range(t):
    if k3[i]==k3[i-1]:
        k2[i]=k2[i-1]
    else:
        k2[i]=d
    d+=1   
for i in range(t):
    for j in range(t):
        if k3[i]==k[j]:
            k_ans[j]= str(k2[i])
print(' '.join(k_ans)) """

#t=int(input())
t=5
n=0
x_lst=[]
y_lst=[]
k=[]
""" while n<t:
    x,y=list(map(int,input().split()))
    x_lst.append(x)
    y_lst.append(y) 
    n+=1"""
x_lst=[55,58,88,60,46]
y_lst=[185,183,186,175,155]
for i in range(t):
    cnt=0
    for j in range(t):
        if x_lst[i]<x_lst[j] and y_lst[i]<y_lst[j]:
            cnt+=1
    k.append(cnt)
print(k)
k2=list(k)
for i in range(t):
    k[i]= str(k2[i]+1)
print(' '.join(k))
