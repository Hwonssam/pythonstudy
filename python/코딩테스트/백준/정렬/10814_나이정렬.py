import sys
t=int(sys.stdin.readline())
lst=[['0'] for i in range(201)]
for i in range(t):
    a,b=input().split()
    lst[int(a)] =lst[int(a)]+ [b]
    
for i in range(201):
    if lst[i] != ['0']:
        for j in range(len(lst[i])-1):
            print(i,lst[i][j+1])

