import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
pis = list()
for i in range(n):
    pis.append( int(input()) )

pis.sort()

diffs = list()

for i in range(n - 1):
    diffs.append(pis[i + 1] - pis[i])

print(min(diffs))
