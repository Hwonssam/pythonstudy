import sys 
n= int(sys.stdin.readline())
lst=[0]*10
for i in range(len(str(n))):
    c=str(n)[i]
    lst[int(c)] +=1
a=''
for i in range(10):
    for _ in range(lst[i]):
        a=str(i)+a
print(a)