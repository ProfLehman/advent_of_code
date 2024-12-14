# me :-)
# 12 December 2024
# j. l. lehman
#

import sys
sys.setrecursionlimit(100000)


def offGrid(r,c):
    return r < 1 or r >= numRows-1 or c < 1 or c >= numCols-1

def countNeighbors(r,c,d):
    count = 0

    if offGrid(r-1,c) == False:
        if data[r-1][c] == d:
            count += 1

    if offGrid(r+1,c) == False:
        if data[r+1][c] == d:
            count += 1
            
    if offGrid(r,c-1) == False:
        if data[r][c-1] == d:
            count += 1

    if offGrid(r,c+1) == False:
        if data[r][c+1] == d:
            count += 1

    return count

def area(r, c, d):

    if data[r][c] != d:
        return 0
    
    key = f"{r},{c}"
    if key not in visited:
        visited[ key ] = True
        checked[ key ] = True

        return 1 + area(r-1, c, d) + area(r+1, c, d) + area(r, c-1, d) + area(r, c+1, d)
    else:
        return 0

def hole(r,c,d):
    if data[r-1][c] != d and data[r+1][c] != d and data[r][c-1] != d and data[r][c+1] != d:
        return True
    else:
        return False

def perimeter(r, c, d):

    key = f"{r},{c}"
    #print( key )
  
    #check for hole
    if hole(r,c,d) == True:
        #print("hole")
        return 4
    
    #regular border
    if offGrid(r,c) or data[r][c] != d:
        #print("regular border - off grid or different")
        if key not in visited:
            visited[key] = True   
            return countNeighbors(r,c,d)
        else:
            return 0
    
    if key not in visited:
        visited[ key ] = True
        return perimeter(r-1, c, d) + perimeter(r+1, c, d) + perimeter(r, c-1, d) + perimeter(r, c+1, d)
    else:
        return 0


# --- Load Data ------------------------------------------------------------------
file = open('AOC_2024/day12/day12t4.txt', 'r')
# --------------------------------------------------------------------------------
r = -1
c = -1
data = []
data = file.readlines()

i = 0
while i < len(data):
    data[i] = "." + data[i].strip() + "."
    #print( data[i] )
    i = i + 1
#print( data )

numCols = len(data[0])
data.insert(0, "." * numCols)
data.append( "." * numCols )

numRows = len(data)
print( f"numRows = {numRows}, numCols = {numCols}")
print(data)
print()


# --- Part I ---
part1 = 0

checked = {}

r = 1
while r < numRows-1:

    c = 1
    while c < numCols-1:

        value = data[r][c]
        key = f"{r},{c}"

        if key not in checked:

            # area
            visited = {}
            a = area(r, c, data[r][c])
    
            # perimeter
            visited = {}
            p = perimeter(r, c, data[r][c])
            print( f"{value} area {a:2} perimeter {p:2}    {a} * {p} = {a*p}" )

            part1 += (a * p)
            
        c += 1
    r += 1


print()
print( "Part I.", part1 ) #too high 1468097