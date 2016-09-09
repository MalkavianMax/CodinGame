import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lon = input()
lat = input()
n = int(input())
defibs = []
for i in range(n):
    defibs.append( str(input()).split(';') )

def norm(val):
    return math.radians(float(str(val).replace(',', '.')))

for defib in defibs:
    deflon = norm(defib[4])
    deflat = norm(defib[5])
    ulon = norm(lon)
    ulat = norm(lat)
    x = (ulon - deflon) * math.cos((ulat + deflat)/2)
    y = (ulat - deflat)
    d = math.sqrt(x**2 + y**2) * 6371
    defib.append(d)
    
defibs.sort(key = lambda defib: float(defib[6]))

print(defibs[0][1])
