# me :-)

file = open('AOC_2024/day5/day5.txt', 'r')

map = {}
data = []

# read rules
line = file.readline().strip()
while line != "":

    # get rule
    values = line.split('|')
    left = int(values[0])
    right = int(values[1])

    # add to map[key] = { set of values }
    if left in map:
        mapData = map.get(left)
        mapData.add( right )
        map[left] = mapData
    else:
        map[left] = {right} #new set

    line = file.readline().strip()

# read data
line = file.readline().strip()
while line != "":
    
    #convert data to int list
    dataLine = line.split(",")
    i = 0
    while i < len(dataLine):
        dataLine[i] = int(dataLine[i])
        i = i + 1

    # add to data list of lists
    data.append( dataLine )

    line = file.readline().strip()
    
file.close()

# --- data ---
print("map")
print( map )
print()
print( "data")
print( data )
print()

# --- part 1 ---
part1 = 0

for line in data:

    # check each line
    lineOK = True

    # start at end of list
    i = len(line)-1
    while i > 0 and lineOK:
        n = line[i]
        if n in map:
            #print( n, "=>", map[n] )
            # make sure no violations
            for c in line[:i]:
                if c in map[n]:
                    lineOK = False
        i = i - 1
    
    if lineOK:
        m = len(line) // 2
        part1 = part1 + line[m]

print("Part 1:", part1)




