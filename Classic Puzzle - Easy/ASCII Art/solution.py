import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()
abc = []
for i in range(h):
    abc.append( input() )

print(t, file=sys.stderr)

for i in range(h):
    outstr = ""
    for c in t:
        o = ord(c)
        if 65 <= o <= 90:
            n = o - 65
        elif 97 <= o <= 122:
            n = o - 97
        else:
            n = 26
        start = l * n
        end   = l * (n + 1)
        outstr += abc[i][start:end]
    print(outstr)