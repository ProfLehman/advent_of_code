# me :-)
# 12 December 2024
# j. l. lehman
#

from operator import itemgetter

import sys
sys.setrecursionlimit(100000)

def countSides( e ):
    count = 0
    #[[3, 2], [3, 3], [3, 4], [3, 5], [4, 1], [4, 6], [5, 2], [5, 3], [5, 4], [5, 5]]

    temp = sorted(edge, key=itemgetter(0))

    temp_n = []
    temp_s = []
    temp_e = []
    temp_w = []

    for v in temp:
        if v[0] == "n":
            temp_n.append(v)
        if v[0] == "s":
            temp_s.append(v)
        if v[0] == "e":
            temp_e.append(v)
        if v[0] == "w":
            temp_w.append(v)

    temp_n = sorted(temp_n, key=itemgetter(1,2))
    temp_s = sorted(temp_s, key=itemgetter(1,2))

    temp_e = sorted(temp_e, key=itemgetter(2,1))
    temp_w = sorted(temp_w, key=itemgetter(2,1))

    print( "north", temp_n )
    print( "south", temp_s )
    print( "east", temp_e )
    print( "west", temp_w )
    
    n_count = 0
    s_count = 0
    e_count = 0
    w_count = 0

    #north
    i = 1
    while i < len(temp_n):
        # same row and column skips
        if temp_n[i][1] == temp_n[i-1][1]  and abs(temp_n[i][2] - temp_n[i-1][2]) != 1:
            n_count = n_count + 1          
        #new side if next row
        elif temp_n[i][1] != temp_n[i-1][1]:
            n_count = n_count + 1 
        i += 1
    n_count += 1

    #south
    i = 1
    while i < len(temp_s):
        # same row and column skips
        if temp_s[i][1] == temp_s[i-1][1]  and abs(temp_s[i][2] - temp_s[i-1][2]) != 1:
            s_count = s_count + 1          
        #new side if next row
        elif temp_s[i][1] != temp_s[i-1][1]:
            s_count = s_count + 1 
        i += 1
    s_count += 1

    #east
    i = 1
    while i < len(temp_e):
        # same column and row skips
        if temp_e[i][2] == temp_e[i-1][2]  and abs(temp_e[i][1] - temp_e[i-1][1]) != 1:
            e_count = e_count + 1          
        #new side if next col
        elif temp_e[i][2] != temp_e[i-1][2]:
            e_count = e_count + 1 
        i += 1
    e_count += 1

    #west
    i = 1
    while i < len(temp_w):
        # same column and row skips
        if temp_w[i][2] == temp_w[i-1][2]  and abs(temp_w[i][1] - temp_w[i-1][1]) != 1:
            w_count = w_count + 1          
        #new side if next col
        elif temp_w[i][2] != temp_w[i-1][2]:
            w_count = w_count + 1 
        i += 1
    w_count += 1

    print(n_count, s_count, e_count, w_count)

    count = n_count + s_count + e_count + w_count
    print( "count: ", count)

    return count

def perimeter(r,c,d):
    count = 0

    if data[r-1][c] != d:
        count += 1
        edge.append( ["n", r, c] )

    if data[r+1][c] != d:
        count += 1
        edge.append( ["s", r, c] )
        
    if data[r][c-1] != d:
        count += 1
        edge.append( ["w",r, c] )

    if data[r][c+1] != d:
        count += 1
        edge.append( ["e", r, c] )

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
    print( data[i] )
    i = i + 1

numCols = len(data[0])
data.insert(0, "." * numCols)
data.append( "." * numCols )
#print( data )
print()

numRows = len(data)
print( f"numRows = {numRows}, numCols = {numCols}")
#print(data)

# --- Part I ---
part1 = 0
part2 = 0

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
            edge = []
            p = 0 #perimeter
            s = 0 #sides
            a = area(r, c, data[r][c])
    
            #print( f"{value} area {a:2} perimeter {p:2}    {a} * {p} = {a*p}" )
            part1 += (a * p)

            s = countSides( edge )            
            print( f"     {value} => area {a}, sides {s},    {a} * {s} = {a*s}" )
            part2 += (a * s)

            print()

        c += 1
    r += 1


print()
print( " Part I.", part1 ) #too high 1468097, 1465968 yes!
print( "Part II.", part2 ) #too high 1468097, 1465968 yes!