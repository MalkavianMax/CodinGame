width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis

# Get the grid
grid = [ list( x for x in input() ) for y in range(height) ]

# Save all nodes from grid into the list
nodes = list()
for y in range(height):
    for x in range(width):
        if grid[y][x] == '0':
            nodes.append(tuple([x, y]))

for n in nodes:
    x2, y2, x3, y3  = ['-1 '] * 4
    # Search neighbors starts with the lower-right conner of the grid,
    # so every closest neighbor will overwrite the previous value
    for nn in nodes[::-1]:
        if nn[0] > n[0] and nn[1] == n[1]:
            x2, y2 = nn[0], nn[1]
        if nn[0] == n[0] and nn[1] > n[1]:
            x3, y3 = nn[0], nn[1]
    print( ' '.join([ str(x) for x in [ n[0], n[1], x2, y2, x3, y3 ] ]) )
