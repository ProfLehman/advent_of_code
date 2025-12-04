# day2.py
#
## me :-)

def has_pattern_1( s ):
    result = False

    if len(s_count) % 2 == 0:
        #print( s_count, len(s_count) )
        half = len(s_count) // 2 # note: integer division
        if s_count[:half] == s_count[half:]:
            result = True

    return result

def has_pattern_2( s ):
    result = False

    slice = 1
    while slice <= (len(s)//2) and result == False:

        if (len(s) % slice) == 0:
            chunks = []
            i = 0

            while i < len(s):
                chunks.append( s[i:i+slice] )
                i = i + slice

            #print(chunks)

            match = True
            first = chunks[0]
            c = 1
            while c < len(chunks) and match == True:
                if chunks[c] != first:
                    match = False
                c = c + 1

            if match:
                result = True

        slice = slice + 1
        #end loop

    return result

part1 = 0
part2 = 0

file = open('AOC_2025/day2/test2.txt', 'r')

data = file.readline().split(",")
#print( data )

for line in data:
    d = line.split("-")
    start = int( d[0] )
    stop = int( d[1] )

    #print( d, start, stop )

    count = start
    while count <= stop:

        s_count = str(count)
        #print( s_count )

        if has_pattern_1(s_count):
            part1 = part1 + count

        if has_pattern_2(s_count):
            print( "yes", s_count )
            part2 = part2 + count

        count = count + 1
        # loop

file.close()

# --- results ---
print()
print("Part 1:", part1)
print("Part 2:", part2)
print()
print( has_pattern_2("11") )

print()


