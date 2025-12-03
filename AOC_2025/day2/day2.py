# day1.py
#
## me :-)

part1 = 0
part2 = 0

position = 50

file = open('AOC_2025/day2/test2.txt', 'r')

data = file.readline().split(",")
print( data )

for line in data:
    d = line.split("-")
    start = int( d[0] )
    stop = int( d[1] )

    print( d, start, stop )

    count = start
    while count <= stop:

        s_count = str(count)
        #print( s_count )

        if len(s_count) % 2 == 0:
            #print( s_count, len(s_count) )
            half = len(s_count) // 2 # note: integer division
            if s_count[:half] == s_count[half:]:
                part1 = part1 + count

        count = count + 1
        # loop

file.close()

# --- results ---
print()
print("Part 1:", part1)
print("Part 2:", part2)
