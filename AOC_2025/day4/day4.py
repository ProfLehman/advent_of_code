
#Part 1:

def count_neighbors( m, a, b):
    count = 0

    rp = [-1, -1, -1, 0, 0, 1, 1, 1]
    cp = [-1, 0, 1, -1, 1, -1, 0, 1]

    x = 0
    while x < len(rp):
        tr = a + rp[x]
        tc = b + cp[x]
        #print( (tr, tc) )
        if (tr,tc) in m:
            count = count + 1
        
        x = x + 1

    return count

# --- main ---

part1 = 0
part2 = 0

file = open('AOC_2025/day4/test2.txt', 'r')

# build sparse matrix
data = {}

r = 0
line = file.readline().strip()
while line != "":
    

    c = 0
    for value in line:
        if value == "@":
            data[(r,c)] = True
        c = c + 1

    num_cols = c
    r = r + 1
    line = file.readline().strip()
    # loop

num_rows = r
file.close()

print( "num rows:", num_rows)
print( "num cols:", num_cols)
print()

#print( data )


for r in range(0, num_rows):
    for c in range(0, num_cols):
        if (r,c) in data:
            print( "@", end="")
        else:
            print( ".", end="") 
    print()
print()

for r in range(0, num_rows):
    for c in range(0, num_cols):
        
        if data.get((r,c)) == True:
            print( count_neighbors(data, r, c), end="")
            if count_neighbors(data, r, c) < 4:
                part1 = part1 + 1
        else:
            print(".", end="")
    print()


change = True
while change == True:
    change = False
    for r in range(0, num_rows):
        for c in range(0, num_cols):
            if data.get((r,c)) == True:
                if count_neighbors(data, r, c) < 4:
                    part2 = part2 + 1
                    data.pop((r,c))
                    change = True

# --- results ---
print()
print("Part 1:", part1)
print("Part 2:", part2)
print()

#print( count_neighbors(data, 3, 0) )

