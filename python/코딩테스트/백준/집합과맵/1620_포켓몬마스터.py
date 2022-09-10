import sys
d,s=list(map(int,input().split()))
d_lst=[[sys.stdin.readline(),i] for i in range(d)]
a=sorted(d_lst)
def bi(array,search):
    l=0
    r=len(array)-1
    while l<=r:
        mid=(l+r)//2
        b=sorted([array[mid][0],search])
        if array[mid][0] == search:
            return array[mid][1]
        elif b[0]==search:
            r=mid-1
        else :
           l=mid+1
for x in range(s):
    i=sys.stdin.readline()
    try :
        print(d_lst[int(i)-1][0],end='')
    except:
        print(bi(a,i)+1)

""" pr = open(0).read().rstrip().split('\n')
n, m = map(int, pr[0].split())

dictionary = dict(zip(pr[1:n+1], range(1, n+1)))

print('\n'.join(map(lambda x: str(dictionary[x]) if x.isalpha() else pr[int(x)], pr[n+1:]))) """