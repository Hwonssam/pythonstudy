t= int(input())
cnt = 0
while cnt < t :
    k=int(input())
    n=int(input())
    cnt +=1
    c =0#층
    d= list(range(1,n+1))
    x=d
    while c<k :
        c+=1
        a=0
        for i in range(n) :
            a += d[i]
            x[i] = a
        d=x
    print(d[n-1])

'''
   1 5  
   1 4  10  20
   1 3  6   10
0층1 2   3  4   5
     1   1   1   1'''
