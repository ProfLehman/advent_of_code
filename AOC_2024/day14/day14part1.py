import re

def displayBots( t, bots, w, h):
    
    print()
    print( f"t: {t}")
    print()

    #build map
    map = {}
    i = 0
    while i < len(bots):
        over = bots[i][0]
        down = bots[i][1]
        key = f"{over},{down}"
        if key in map:
            value = map[key]
            value += 1
            map[key] = value
        else:
            map[key] = 1

        i += 1

    #print bots
    down = 0
    while down < h:
        over = 0
        while over < w:
            key = f"{over},{down}"
            if key in map:
                print(map[key], end="")
            else:
                print(".", end="")
            over = over + 1
        print()
        down = down + 1
    print()
    print()



# --- Load Data ------------------------------------------------------------------
file = open('AOC_2024/day14/day14p2.txt', 'r')
# ------------------------------------------------------------------------------

part1 = 0
part2 = 0

bots = []

pattern = r"[-+]?\d+"

data = file.readlines()
i = 0
while i < len(data):
    temp = re.findall(pattern, data[i].strip())
    bots.append( [ int(temp[0]), int(temp[1]), int(temp[2]), int(temp[3]) ] )
    i = i + 1

#-----------------------
print( bots )
print()

width = 101 #11
height = 103 #7

midOver = width // 2
midDown = height // 2

print(width, midOver, height, midDown)
print()

displayBots( 0, bots, width, height)

# move bots 100 seconds
t = 1
while t <= 100:
    i = 0
    while i < len(bots):
        #move bot
        bots[i][0] = (bots[i][0] + bots[i][2]) % width
        bots[i][1] = (bots[i][1] + bots[i][3]) % height
        i += 1

    displayBots( t, bots, width, height)
    t += 1

# count bots in quadrants
q1 = 0
q2 = 0
q3 = 0
q4 = 0
"""
q1 | q2
---+---
q4 | q3

"""
for bot in bots:
    over = bot[0]
    down = bot[1]

    if over < midOver and down < midDown:
        q1 += 1
    
    if over < midOver and down > midDown:
        q4 += 1
    
    if over > midOver and down < midDown:
        q2 += 1
    
    if over > midOver and down > midDown:
        q3 += 1
    
print()
print(q1, q2, q3, q4)
part1 = q1 * q2 * q3 * q4

print()    
print( " Part I: ", part1 ) #232253028 first try :-)
print( "Part II: ", part2 ) 