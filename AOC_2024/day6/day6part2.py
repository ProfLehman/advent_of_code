# me :-)
# 6 December 2024
# j. l. lehman
#

# needed for recursion approach
#import sys
#sys.setrecursionlimit(100000)

blockRow = -1
blockCol = -1

def offGrid(r,c):
    return r < 0 or r >= numRows or c < 0 or c >= numCols

def tempBlock(r,c):
    #print(f"in tempBlock {r},{c} and blocked is {blockRow}, {blockCol}")
    temp = (r == blockRow and c == blockCol)
    #if temp:
    #   print( "blocked", r, c)
    return temp

def isBlocked(r, c, d):
    blocked = False

    if d == "n":
        if offGrid(r-1,c) == False:
            if data[r-1][c] == "#" or tempBlock(r-1,c):
                blocked = True
    elif d == "e":
        if offGrid(r,c+1) == False:
            if data[r][c+1] == "#" or tempBlock(r,c+1):
                blocked = True
    elif d == "s":
        if offGrid(r+1,c) == False:
            if data[r+1][c] == "#" or tempBlock(r+1,c):
                blocked = True
    elif d == "w":
        if offGrid(r,c-1) == False: 
            if data[r][c-1] == "#" or tempBlock(r,c-1):
                blocked = True
    else:
        print("Error in isBlocked")

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
startRow = r
startCol = c
print()

"""
# recursive approach
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
"""
        
# non-recursive approach
def patrol(r, c, d):

    while offGrid(r,c) == False:

        map[ f"{r},{c}" ] = True

        while isBlocked(r,c,d):
            d = turn(d)

        if d == "n":
            r = r - 1
        elif d == "s":
            r = r + 1
        elif d == "e":
            c = c + 1
        else:
            c = c - 1

        #end loop

# --- Part I ---
# If there is something directly in front of you, turn right 90 degrees.
# Otherwise, take a step forward.

patrol( r, c, d)

print( "Part I.", len(map) ) #5551 part 1 ... whooo hooo ...
print()

#print( map )


# --- Part II ---

def walk(r, c, d):

    tempMap = {}
    stuck = False

    while offGrid(r,c) == False and stuck == False:

        #print(f"walking {r},{c},{d}")

        key = f"{r},{c},{d}"

        if key in tempMap:
            stuck = True
            #print("Stuck ...")
        else:
            tempMap[key] = True


            while isBlocked(r,c,d):
                d = turn(d)

            if d == "n":
                r = r - 1
            elif d == "s":
                r = r + 1
            elif d == "e":
                c = c + 1
            else:
                c = c - 1

        #end loop
    #if not stuck:
    #    print("Made it ... done walking")
    return stuck

# count of blocks
part2 = 0

for m in map:
    
    #get row and col
    temp = m.split(",")
    tempRow = int(temp[0])
    tempCol = int(temp[1])
    
    if tempRow != startRow or tempCol != startCol:
        #print( f"{m} => {tempRow},{tempCol}" )

        r = startRow
        c = startCol
        d = "n"

        blockRow = tempRow
        blockCol = tempCol
        #print( "before call to walk", blockRow, blockCol)

        if walk( r, c, d) == True:
            part2 += 1

print( f"Part II.  {part2}" ) #1939 ... yes!

#blockRow = 6
#blockCol = 3
#print( walk(startRow, startCol, "n") )

    