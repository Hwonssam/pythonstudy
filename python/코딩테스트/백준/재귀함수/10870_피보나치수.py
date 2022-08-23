n=10
def pivo(n) :
    if n<=1:
        return n
    return pivo(n-1)+pivo(n-2)
        
        

print(pivo(n))