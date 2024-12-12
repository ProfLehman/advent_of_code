#
# day11 - part 2
#

def next_stones( temp_stones, rounds ):

    for _ in range(0,rounds):
        new_stones = []
        
        for s in temp_stones:
            if s == 0:
                new_stones.append(1)

            elif len(str(s)) % 2 == 0:
                temp = str(s)
                half = len(temp)//2
                new_stones.append( int(temp[:half]) )
                new_stones.append( int(temp[half:]) )
            else:
                new_stones.append( s * 2024)
        #print( new_stones )
        temp_stones = new_stones
    return temp_stones

def iterate( s, n):
    #print( "iterate:", s, n)
    temp_count = 0

    # base case - return count of items in map
    if n == 1:
        
        temp_items = map[s]
        i = 0
        while i < len(temp_items):
            temp_count += temp_items[i]
            i += 2
    else:
        temp_items = map[s]
        i = 0
        while i < len(temp_items):
            temp_count += temp_items[i] * iterate(temp_items[i+1], n-1)
            i += 2

    return temp_count

# ---------------------------------------------------------------
stones = [0, 27, 5409930, 828979, 4471, 3, 68524, 170]
#stones = [125, 17]
#stones = [0]
# ---------------------------------------------------------------

# --- build map with all x5 values ---
map = {}
queue = stones.copy()
while len(queue) > 0:

    new_items = []    
    for item in queue:

        if item not in map:
            new_stones = next_stones( [item], 25 ) # get five map for item
            map[item] = new_stones # store in map
            for stone in new_stones: # add results to queue to check if not already found
                if stone not in map:
                    new_items.append(stone)

    # place new items in queue
    queue = []
    for item in new_items:
        queue.append(item)

    print( "Map size,", len(map), len(queue) )
    print()

# --- update map format 
# 0 [4048, 1, 4048, 8096]
# m[0] => 2, 4048, 1, 1, 1, 8096
for m in map:
    #print( "current", map[m] )
    temp_map = {}
    for item in map[m]:
        if item in temp_map:
            current_count = temp_map[item]
            current_count += 1
            temp_map[item] = current_count
        else:
            temp_map[item] = 1

    temp = []
    for item in temp_map:
        temp.append(temp_map[item]) #number of items
        temp.append(item) #item
    map[m] = temp.copy()

    print( m, "updated", map[m] )
    print()

print()

# --- iterate ---


part2 = 0
s = 3

#part2 += iterate( 125, 5)
#part2 += iterate( 17, 5)

#t1 = [125, 17]
#for t in t1:
#    part2 = part2 + iterate(t, s)

t1 = [27, 0, 5409930, 828979, 4471, 3, 68524, 170]
for t in t1:
    part2 = part2 + iterate(t, s)
    print( part2 )


print( "Part 2:", part2 ) #solved 232454623677743
print()
