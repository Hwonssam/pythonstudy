a= int(input())
b=1 #총갯수
c=1 #대각선수
d=0 #진행방향
answer=0
while True :
    if a > b :
        c+=1
        b+=c
        d+=1
    elif d%2 ==1 :
        print(f"{(a-b+c)}/{(b-a+1)}")
        break
    else :
        print(f"{(b-a+1)}/{(a-b+c)}")
        break
''' 다른풀이
n=int(input())
i=1
while n>i:
  n-=i
  i+=1

if i%2==0:
  print(f"{n}/{i+1-n}")
else:
  print(f"{i-n+1}/{n}")
  '''