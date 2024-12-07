# me :-)
# 6 December 2024
# j. l. lehman
#

import sys

sys.setrecursionlimit(100000)


def offGrid(r,c):
    return r < 0 or r >= numRows or c < 0 or c >= numCols

def isBlocked(r, c, d):
    blocked = False

    if d == "n":
        if offGrid(r-1,c) == False:
            if data[r-1][c] == "#":
                blocked = True
    elif d == "e":
        if offGrid(r,c+1) == False:
            if data[r][c+1] == "#":
                blocked = True
    elif d == "s":
        if offGrid(r+1,c) == False:
            if data[r+1][c] == "#":
                blocked = True
    else:
        if offGrid(r,c-1) == False:
            if data[r][c-1] == "#":
                blocked = True

    return blocked

def turn(d):
    if d == "n":
        d = "e"
    elif d == "e":
        d = "s"
    elif d == "s":
        d = "w"
    else:
        d = "n"
    return d

# --- Load Data ---
file = open('AOC_2024/day6/day6.txt', 'r')

# position of guard
r = -1
c = -1
d = "n"

data = []
map = {}

data = file.readlines()
i = 0
while i < len(data):

    data[i] = data[i].strip()

    if "^" in data[i]:
        r = i
        c = data[i].find("^") 
        data[i] = data[i].replace("^", ".")

    print( data[i] )

    i = i + 1

#print( data )

numRows = len(data)
numCols = len(data[0])
print( f"numRows = {numRows}, numCols = {numCols}")
print( f"carrot at {r},{c}")
print()

def patrol(r, c, d):

    if offGrid(r,c) == False:

        map[ f"{r},{c}" ] = True

        while isBlocked(r,c,d):
            d = turn(d)

        if d == "n":
            patrol(r-1, c, d)
        elif d == "s":
            patrol(r+1, c, d)
        elif d == "e":
            patrol(r, c+1, d)
        else:
            patrol(r, c-1, d)

        


# --- Part I ---
# If there is something directly in front of you, turn right 90 degrees.
# Otherwise, take a step forward.

patrol( r, c, d)

print( "Part I.", len(map) ) #5551 part 1 ... whooo hooo ...
#print( map )