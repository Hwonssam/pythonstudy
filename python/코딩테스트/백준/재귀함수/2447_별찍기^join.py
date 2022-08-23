from array import array


def star(n):
    if n ==3:
        return ['***','* *','***']
    stars=[]
    arr = star(n//3)
    for i in arr:
        stars.append(i*3)
    for i in arr:
        stars.append(i+' '*(n//3)+i)
    for i in arr:
        stars.append(i*3)
    return stars

n=9

print('\n'.join(star(n)))
