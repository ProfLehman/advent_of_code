# day5.py
# all me
#
# had to think a day on part 2, but illustrates the value of letting problems "perculate"
#

# --- main ---

part1 = 0
part2 = 0

file = open('AOC_2025/day5/test2.txt', 'r')

start = []
stop = []

line = file.readline().strip()
while line != "":
    
    temp = line.split("-")
    start.append( int(temp[0]) )
    stop.append( int(temp[1]) )

    line = file.readline().strip()
    # loop

id = []
id_found = []

line = file.readline().strip()
while line != "":
    id.append( int(line) )
    id_found.append( False )
    line = file.readline().strip()
    # loop

file.close()

#print( start )
#print( stop )
#print( id )
print(len(start))
print(len(id))

# check each id
i = 0
while i < len(id):

    # check id in each range
    x = 0
    while id_found[i] == False and x < len(start):
        
        if id[i] >= start[x] and id[i] <= stop[x]:
            id_found[i] = True
            part1 = part1 + 1
        x = x + 1

    i = i + 1

# print( id_found )

"""
# memory map too large, ran out of memory :-(
map = {}

x = 0
while x < len(start):

    count = start[x]
    while count <= stop[x]:
        map[ count ] = True
        count = count + 1

    x = x + 1

part2 = len( map )
"""

print( start )
print( stop )

# bubble sort start and stop
for a in range(0, len(start)-1):
    for b in range(0, len(start)-1):
        if start[b] > start[b+1]:
            temp = start[b+1]
            start[b+1] = start[b]
            start[b] = temp

            temp = stop[b+1]
            stop[b+1] = stop[b]
            stop[b] = temp

print()
print( start )
print( stop )

# note: could streamline following code now that ranges are sorted, but it worked :-)

# merge start/stop lists by range
start_2 = [ start[0] ]
stop_2 = [ stop[0] ]

x = 1
while x < len(start):

    done = False
    y = 0
    while y < len(start_2) and done == False:

        # fits in current, thus do not add 
        if start[x] >= start_2[y] and stop[x] <= stop_2[y]:
            done = True
        
        # encompasses current, thus change start and stop
        elif start[x] <= start_2[y] and stop[x] >= stop_2[y]:
            done = True
            start_2[y] = start[x]
            stop_2[y] = stop[x]

        # left less, right within, update start 
        elif start[x] <= start_2[y] and (stop[x] >= start_2[y] and stop[x] <= stop_2[y]):
            done = True
            start_2[y] = start[x]

        # left within, right greater, update stop  
        elif (start[x] >= start_2[y] and start[x] <= stop_2[y]) and stop[x] > stop_2[y]:
            done = True
            stop_2[y] = stop[x]

#        print( start_2 )
#        print( stop_2 )
#        print()

        y = y + 1
        # loop through start_2

    if done == False:
        start_2.append( start[x] )
        stop_2.append( stop[x] )

    x = x + 1
    # loop through start/stop

print( start_2 )
print( stop_2 )
print()

# add numbers in range
for a in range(0, len(start_2)):
    part2 = part2 + (stop_2[a] - start_2[a] + 1)


# --- results ---
print()
print("Part 1:", part1)
print("Part 2:", part2)
print()
