import sys
n= int(sys.stdin.readline())
def fac(n):
    if n<=1:
        return 1
    else:
        return fac(n-1)*n

print(fac(n))