import sys
while True :
    n= int(sys.stdin.readline())
    if n == 0:
        break
    pn = [True for i in range(2*n+1)]
    pn[0]= False
    pn[1]= False
    p = 2
    while (p*p <= 2*n):
        if (pn[p]):
            for i in range(p*p, 2*n+1, p):
                pn[i] = False
        p += 1
    print(pn[n+1:].count(True))