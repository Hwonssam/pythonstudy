""" from sys import stdin,stdout
n=int(stdin.readline())
array=[]
while len(array) <n:
    a=int(stdin.readline())
    array.append(a)
array.sort()
stdout.write('\n'.join(map(str,array))) """

import sys
n= int(sys.stdin.readline())
num=[0]*10001
for i in range(n):
    num[int(sys.stdin.readline())] +=1
for i in range(1,10001):
    for _ in range(num[i]):
        print(i)