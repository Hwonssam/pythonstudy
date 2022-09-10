import sys
def binarySearch(array, value):
    low=0
    high=len(m)-1
    
    while low <= high:
        mid =(low+high) / 2
        if array[mid] > value :
            high = mid -1
        elif array[mid] < value :
            low = mid +1
        else:
            return mid

t=int(sys.stdin.readline())
n=list(map(int,sys.stdin.readline().split()))
m=sorted(set(n))
for i in n:
    print(binarySearch(m, i), end=' ')

'''다른풀이
dic={m[a]:a for a in range(len(m))}

for i in range(0,t):
    print(dic[n[i]],end=" ")
'''

"""import sys

# input
sys.stdin.readline()
X_list = list(map(int, sys.stdin.readline().split()))

#sort
X_dict = {ele: idx for idx, ele in enumerate(sorted(set(X_list)))}

#output
print(' '.join(map(str, [X_dict[ele] for ele in X_list])))"""