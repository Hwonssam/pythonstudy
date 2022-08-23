import sys

a = sys.stdin.readlines()[1:]
a.sort(key = lambda a : (int(a.split()[1]), int(a.split()[0])))
print("".join(a))

