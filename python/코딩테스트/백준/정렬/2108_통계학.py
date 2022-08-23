from sys import stdin, stdout

n=int(stdin.readline())
num=[0]*8001
c=0
for i in range(n):
    a=int(stdin.readline())
    num[a-4001] +=1
    c+=a
cnt=0
k=1
often=-4001
cnt2=True
for i in range(8001):
    if num[i]>often:
            often = num[i]
            often2= i-4000
            cnt2=True
    elif num[i]==often and cnt2==True:
            often2= i-4000
            cnt2= False
    for _ in range(num[i]):
        cnt+=1
        if cnt==1:
            min=i-4000
        if cnt==(n+1)/2:
            cen=i-4000
        if cnt==n:
            max=i-4000
print(round(c/n))
print(cen)
print(often2)
print(max-min)