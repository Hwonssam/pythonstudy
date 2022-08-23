from re import I


a=int(input())
for i in range(2,a+1):
    while a%i == 0:
            a=a/i
            print(i)

""" 다른사람풀이
n = int(input())
d = 2
while d*d <= n:
    if n % d == 0:
        print(d)
        n //= d
    else:
        d += 2 if d > 2 else 1
if n > 1:
    print(n) """