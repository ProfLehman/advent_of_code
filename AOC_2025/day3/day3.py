# day3.py
#
## me :-)

def joltage( s ):

    result = 0

    # convert to list
    data = []
    for digit in s:
          data.append( int(digit) )

    # first_position
    first_postion = 0
    x = 1
    while x < len(data) - 1:
        if data[x] > data[first_postion]:
            first_postion = x
        x = x + 1

    # second_position
    second_postion = first_postion + 1
    x = first_postion + 2
    while x < len(data):
        if data[x] > data[second_postion]:
            second_postion = x
        x = x + 1

    result = data[first_postion] * 10 + data[second_postion]

    #print( data[first_postion], data[second_postion], result )
    return result


def joltage_2( s, n ):

    result = 0

    # convert to list
    data = []
    for digit in s:
          data.append( int(digit) )


    positions = []
    last_position = -1

    # get highest digit n items back
    back = n-1
    count = 0
    while count < n:
        
        next_position = last_position + 1
        x = next_position + 1
        while x < len(data) - back:
            if data[x] > data[next_position]:
                next_position = x
            x = x + 1

        positions.append(next_position)

        last_position = next_position
        back = back - 1

        count = count + 1
         # loop

    #print( positions )

    # convert to result - positions holds index of digits to use
    multiplier = 1
    i = len(positions) - 1
    while i >= 0:
        result = result + (multiplier * data[positions[i]])
        multiplier = multiplier * 10
        i = i - 1
    
    #print( line, result )
    return result


part1 = 0
part2 = 0

file = open('AOC_2025/day3/test2.txt', 'r')

line = file.readline().strip()
while line != "":

        part1 = part1 + joltage(line)
        part2 = part2 + joltage_2(line, 12)

        line = file.readline().strip()
        # loop

file.close()

# --- results ---
print()
print("Part 1:", part1)
print("Part 2:", part2)
print()





