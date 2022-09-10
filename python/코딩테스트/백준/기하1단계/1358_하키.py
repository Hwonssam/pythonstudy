w,h,x1,y1,p=map(int,input().split())
cnt=0
for i in range(p):
        x2,y2=map(int,input().split())
        if (x1-x2)**2+(y2-y1-h/2)**2<=(h/2)**2 or ((x2-x1)<=w and (x2-x1>=0)\
        and y2-y1>=0 and y2-y1<=h) or (x1+w-x2)**2+(y2-y1-h/2)**2<=(h/2)**2:
            cnt+=1  
print(cnt)