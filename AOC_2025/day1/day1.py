# day1.py
#
## me :-)

part1 = 0
part2 = 0

position = 50

file = open('AOC_2025/test2.txt', 'r')

# read moves
line = file.readline().strip()
while line != "":

    # get move
    move = line[0]
    number = int( line[1:] )

    while number > 99:
        number = number - 100
        part2 = part2 + 1

    start_position = position

    if move == "L":
        if number > position:
            position = 100 - (number - position)
            if position != 0 and start_position != 0:
                part2 = part2 + 1
        else:
            position = position - number
    else:
        if (number + position) > 99:
            position = (number + position) - 100 
            if position != 0 and start_position != 0:
                part2 = part2 + 1
        else:
            position = position + number

    

    if position == 0:
        part1 = part1 + 1
        part2 = part2 + 1
        
    print( move, number, position, part2 )

    line = file.readline().strip()
    # end loop

file.close()

# --- part 1 ---
print()
print("Part 1:", part1)
print("Part 2:", part2)
