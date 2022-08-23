# t=int(input())
# lst=[]
# for i in range(t):
#     a=list(map(int,input().split()))
#     lst.append(a)
# lst2 = sorted(lst)
# for i in lst2:
#     print(i[0],i[1])
import sys
t=int(sys.stdin.readline())
lst=[[-100002] for i in range(200001)]
for i in range(t):
    a,b=list(map(int,sys.stdin.readline().split()))
    lst[a+100000].append(b)

for i in range(200001):
    if lst[i] != [-100002]:
        lst[i].sort()
        for j in range(len(lst[i])-1):
            print(i-100000,lst[i][j+1])

