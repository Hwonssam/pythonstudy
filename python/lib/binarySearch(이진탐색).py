def binarySearch(array, value):
    low=0
    high=len(array)-1
    
    while low <= high:
        mid =(low+high) // 2
        if array[mid] > value :
            high = mid -1
        elif array[mid] < value :
            low = mid +1
        else:
            return mid

#문자열탐색
def bi(array,search):
    l=0
    r=len(array)-1
    while l<=r:
        mid=(l+r)//2
        a=sorted([array[mid],search])
        if array[mid] == search:
            return 1
        elif a[0]==search:
            r=mid-1
        else :
           l=mid+1
    return 0