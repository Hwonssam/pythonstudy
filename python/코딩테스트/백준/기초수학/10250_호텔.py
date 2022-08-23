import math
t= int(input())
cnt = 0
while cnt < t   : 
    h,w,n = list(map(int,input().split()))
    if n%h != 0:
        print(f"{n%h}{str((math.ceil(n/h))).zfill(2)}")
    else:
        print(f"{h}{(str(math.ceil(n/h))).zfill(2)}")
    cnt +=1

