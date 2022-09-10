def binarySearch(array, value):
    low=0
    high=len(array)-1
    
    while low <= high:
        mid =(low+high) // 2
        if array[mid] == value :
            return 1
        elif array[mid] < value :
            low = mid +1 
        else:
            high = mid -1
    return 0

import sys

s = int(sys.stdin.readline())
s_lst = list(map(int, sys.stdin.readline().split()))
c = int(sys.stdin.readline())
c_lst = list(map(int, sys.stdin.readline().split()))

s_lst.sort()
for i in c_lst:
    print(binarySearch(s_lst,i),end=' ')