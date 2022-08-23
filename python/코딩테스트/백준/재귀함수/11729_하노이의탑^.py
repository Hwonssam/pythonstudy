def hanoi_tower(n,from_,to,other):
    global a
    a+=1
    if n==1:
        return 
    hanoi_tower(n-1,from_,other,to)
    hanoi_tower(n-1,other,to,from_)
n=int(input())
i=n
a=0
hanoi_tower(n,1,2,3)
print(a)

def hanoi_tower2(i,from_,to,other):
    if i==1:
        print(from_,to)
        return 
    hanoi_tower2(i-1,from_,other,to)
    print(from_,to)
    hanoi_tower2(i-1,other,to,from_)

hanoi_tower2(i,1,3,2)