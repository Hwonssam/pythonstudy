'''1 7 19 37 61
6 12 18 24
 6 6 6 6 '''

t=int(input())
answer= 1
a= 6
b= 1
while True :
    if t > b :
        b += a
        a += 6 #a -> 6
        print(b)
        answer +=1
    else:
        break

print(answer)
    
