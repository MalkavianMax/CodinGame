import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.

mimes = {}
names = list()

for i in range(n):
    ext, mt = input().split()
    mimes[str(ext).lower()] = mt
for i in range(q):
    names.append(input())

for name in names:
    i = str(name).rfind('.')
    print(i, file=sys.stderr)
    if i < 0:
        print('UNKNOWN')
    else:
        ext = name[i+1:]
        mime = mimes.get(str(ext).lower())
        if mime == None:
            print('UNKNOWN')
        else:
            print(mime)
