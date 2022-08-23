import sys
import math
a,b,h=list(map(int,sys.stdin.readline().split())) #input대신 실행시간 줄이기
answer = 0
c=a-b
answer = math.ceil((h-a)/c)+1 #미리막대기에서 a를 빼버린다
print(answer)

''' 3, 1, 5 = 2.5 2'''
''' 5 1 6 = 1.5 2'''
''' 99 98 100 = 100 2
5 3 6 = 2
5 3 11 = 4
7 4 11 = 3'''