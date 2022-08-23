import sys

a = sys.stdin.readlines()[1:]
a=list(set(a))
a.sort(key = lambda a : (len(a),a))
print("".join(a))