while True:
    x,y,z=list(map(int,input().split()))
    if x==0 and y==0 and z==0:
        break
    if x*x+y*y==z*z:
        print('right')
    elif x*x==y*y+z*z:
        print('right')
    elif x*x+z*z==y*y:
        print('right')
    elif x==0 or y==0 or z==0:
        print('wrong')
    else :
        print('wrong')
        
