'''3 5 = 3 6 9 12 15, 5 10 15'''
""" 3   5   6   8   9 
            3   5  3:2  5 3 3:3 
            10     11      12    14       15     16 
            5:2   5:1 3:2  3:4   5:1 3:3  5:3    5:2 3:2
            17     18    19    20    21    22 
            5 3:4
            23     24     25     26     27     28     29     30 """

n=int(input())
cnt=0
for x in range(n//3+1):
    a=x
    y= (n-3*x)/5
    if y%1==0 :
        c=0
        break
    else :
        c=-1
while a > 15:
    a-=15
    y+=3
if c == -1 :
    print(c)
else :
    print("{0:.0f}".format(a+y))


#다른사람풀이
""" N = int(input())
cnt = 0
while True:
    if (N % 5) == 0:
        cnt = cnt + (N // 5)
        print(cnt)
        break
    N -= 3
    cnt += 1
    if N < 0:
        print(-1)
        break """



