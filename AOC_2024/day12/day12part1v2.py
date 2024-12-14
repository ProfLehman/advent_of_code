# me :-)
# 12 December 2024
# j. l. lehman
#

import sys
sys.setrecursionlimit(100000)

def perimeter(r,c,d):
    count = 0

    if data[r-1][c] != d:
        count += 1

    if data[r+1][c] != d:
        count += 1
        
    if data[r][c-1] != d:
        count += 1

    if data[r][c+1] != d:
        count += 1

    return count

def area(r, c, d):
    global p

    if data[r][c] != d:
        return 0
    
    key = f"{r},{c}"
    if key not in visited:
        visited[ key ] = True
        checked[ key ] = True
        p = p + perimeter(r,c,d)

        return 1 + area(r-1, c, d) + area(r+1, c, d) + area(r, c-1, d) + area(r, c+1, d)
    else:
        return 0

# --- Load Data ------------------------------------------------------------------
file = open('AOC_2024/day12/day12.txt', 'r')
# --------------------------------------------------------------------------------
r = -1
c = -1
data = []
data = file.readlines()

i = 0
while i < len(data):
    data[i] = "." + data[i].strip() + "."
    i = i + 1

numCols = len(data[0])
data.insert(0, "." * numCols)
data.append( "." * numCols )

numRows = len(data)
print( f"numRows = {numRows}, numCols = {numCols}")
#print(data)

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
            p = 0 #perimeter
            a = area(r, c, data[r][c])
    
            print( f"{value} area {a:2} perimeter {p:2}    {a} * {p} = {a*p}" )
            part1 += (a * p)
            
        c += 1
    r += 1


print()
print( "Part I.", part1 ) #too high 1468097, 1465968 yes!