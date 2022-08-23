total=int(input())
n=int(input())
for i in range(n):
    a,b=list(map(int,input().split()))
    total -= a*b
if total == 0:
    print("Yes")
else :
    print("No")