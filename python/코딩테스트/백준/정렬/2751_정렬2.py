import sys
t=int(sys.stdin.readline())
a=0
lst=[]
while a < t:
    n=int(sys.stdin.readline())
    lst.append(n)
    a+=1
lst.sort()
for i in lst:
    print(i)
#다른사람풀이
""" from sys import stdin, stdout
input()
arr = sorted(list(map(int, stdin.read().split())))
stdout.write('\n'.join(map(str,arr))) """