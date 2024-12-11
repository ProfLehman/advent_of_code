# me :-)
# 10 December 2024
# j. l. lehman
#

import sys
sys.setrecursionlimit(100000)


def offGrid(r,c):
    return r < 0 or r >= numRows or c < 0 or c >= numCols

def hike(r,c,v):
    if not offGrid(r,c):
        if int(data[r][c]) == v+1:
            if int(data[r][c]) == 9:
                map[ f"{r},{c}" ] = True
            else:
                hike(r-1,c,v+1)
                hike(r+1,c,v+1)
                hike(r,c-1,v+1)
                hike(r,c+1,v+1)


# --- Load Data ---
file = open('AOC_2024/day10/day10.txt', 'r')

data = []

data = file.readlines()
i = 0
while i < len(data):
    data[i] = data[i].strip()
    print( data[i] )
    i = i + 1

numRows = len(data)
numCols = len(data[0])
print( f"numRows = {numRows}, numCols = {numCols}")
print()

# --- find trailheads ---
part1 = 0

map = {}
r = 0
for row in data:
    c = 0
    while c < len(row):
        if data[r][c] == "0":
            print( f"trailhead: {r},{c}")
            hike(r,c,-1)
            part1 = part1 + len(map)
            map = {}
        c = c + 1
    r = r + 1

print("Part 1: ", part1)
