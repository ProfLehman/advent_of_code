# me :-)
# 6 December 2024
# j. l. lehman
#
from itertools import combinations
import math

def offGrid(r,c):
    return r < 0 or r >= numRows or c < 0 or c >= numCols

# --- Load Data ---
file = open('AOC_2024/day8/day8.txt', 'r')

# position of guard
map = {}
numRows = 0
numCols = 0

data = file.readline()
r = 0
while data:
    
    data = data.strip()
    numCols = len(data)

    print( data ) 

    #process data line
    c = 0
    while c < numCols:
        if data[c] != ".":
            if data[c] in map:
                points = map[data[c]]
                points.append( f"{r},{c}")
                map[data[c]] = points
            else:
                map[data[c]] = [f"{r},{c}"]
        c += 1     

    r = r + 1
    data = file.readline()

#print( data )
numRows = r
print( f"numRows = {numRows}, numCols = {numCols}")
print()


# --- Part I ---

print( "Part I." ) 
part1 = 0
umap = {}

for m in map:
    print( m, map[m] )
    pairs = combinations(map[m], 2)
    for p in pairs:
        #print( p[0], p[1] )
        a = int(p[0].split(",")[0])
        b = int(p[0].split(",")[1])
        c = int(p[1].split(",")[0])
        d = int(p[1].split(",")[1])
        print( a, b, c, d)

        rowDistance = abs(a - c )
        colDistance = abs(b - d )
        print( rowDistance, colDistance)

        # Calculate horizontal and vertical differences
        delta_x = c - a
        delta_y = d - b

        # Calculate new points
        e = a - delta_x
        f = b - delta_y

        x = e
        y = f
        if x >= 0 and x < numRows:
            if y >= 0 and y < numCols:
                key = f"{x},{y}"
                part1 += 1
                if key not in umap:
                    umap[key] = True

        g = c + delta_x
        h = d + delta_y

        x = g
        y = h
        if x >= 0 and x < numRows:
            if y >= 0 and y < numCols:
                key = f"{x},{y}"
                part1 += 1
                if key not in umap:
                    umap[key] = True
    #print()

print("Part 1: ", part1) #
print("Part 1: ", len(umap) ) #277 too high, 276 - yes!

    