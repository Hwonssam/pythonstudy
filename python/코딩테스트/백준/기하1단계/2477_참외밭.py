num=int(input())
lst=[]
x=[]
y=[]
small=[]
for i in range(6):
    a,b=list(map(int,input().split()))
    lst.append([a,b])
    if a==1 or a==2:
        y.append(b)
    else:
        x.append(b)
x,y=max(x),max(y)
for i in range(6):
    if lst[i][1] != x and lst[i][1] != y:
        if i <=4 and (lst[i-1][1] != x and lst[i+1][1] != x and lst[i+1][1] != y and lst[i-1][1] != y) :
            small.append(lst[i][1])
        elif i == 5 and lst[0][1] != x and lst[0][1] != y and lst[i-1][1] != y and (lst[i-1][1] != x) :
            small.append(lst[i][1])
print((x*y-small[0]*small[1])*num)
""" 
다른사람풀이
n=int(input())
x=[int(input().split()[1])for _ in range(6)]*2
i=x.index(max(x))
j=x.index(max(x[i-1],x[i+1]))
print(n*(x[i]*x[j]-x[i+3]*x[j+3])) """