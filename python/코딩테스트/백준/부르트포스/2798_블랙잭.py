import sys
##n,m=list(map(int,sys.stdin.readline().split()))
#lst=list(map(int,sys.stdin.readline().split()))
n=10
m=500
lst=[93,181,245,214,315,36,185,138,216,295]
lst.sort(reverse=True)
c=0
sum_3=0
ans=0
for i in range(len(lst)):
    lst2=lst[i+1:]
    for j in range(len(lst2)):
        lst3=lst2[j+1:]
        for k in range(len(lst3)):
            sum_3=[lst[i],lst2[j],lst3[k]]
            if sum(sum_3) > ans and sum(sum_3) <=m:
                ans= sum(sum_3)
            if ans==m:
                break
        if ans==m:
            break
    if ans==m:
        break
print(ans)

