
# gpsCount
def gpsCount( map ):
    count = 0
    for m in map:
        if map[m] == "O":
            over = int(m.split(",")[0])
            down = int(m.split(",")[1])
            count = count + (down * 100 + over)
    return count

def display(map):
    down = 0
    while down < height:
        over = 0
        while over < width:
            print( map[f"{over},{down}"], end="")
            over += 1
        print()
        down += 1
    print()

# --- Load Data ------------------------------------------------------------------
file = open('AOC_2024/day15/day15t0.txt', 'r')
# --------------------------------------------------------------------------------

# read maze
first = True
over = 0
down = 0
robotOver = -1
robotDown = -1
map = {}
moves = []
width = -1
height = -1

data = file.readline()
width = len(data.strip())
while data:
    #print( data )
    data = data.strip()
    

    if data[0] == "N":
        first = False
        data = file.readline().strip()

    if first == True:
        over = 0
        while over < len(data):
            map[f"{over},{down}"] = data[over] 

            if data[over] == "@":
                robotOver = over
                robotDown = down
            over += 1
        down = down + 1
        height = down
    else:
        if len(data) > 0:
            for d in data:
                moves.append( d )

    data = file.readline()
    #while data
    
print("width", width, "height", height)
#print("map: ", map)
print()
#print("moves: ", moves)
print()
print(f"robot at {robotOver}, {robotDown}")
print()

# --- process moves ---
count = 0
for m in moves:
    count += 1
    #print( count, m )
    # direction for robot
    move_symbols = "><^v"
    over_options = [1, -1, 0, 0]
    down_options = [0, 0, -1, 1]
    position = move_symbols.find(m)
    over_adj = over_options[ position ] 
    down_adj = down_options[ position ] 
    #print( m, over_adj, down_adj)

    if position == -1:
        print(f"error {count} |{m}|")

    # if open space, move robot one s
    next_over = robotOver + over_adj
    next_down = robotDown + down_adj

    if map[f"{next_over},{next_down}"] == "#":
        wall = True
    elif map[f"{next_over},{next_down}"] == ".":
        map[f"{next_over},{next_down}"] = "@"
        map[f"{robotOver},{robotDown}"] = "."
        robotOver = next_over
        robotDown = next_down
    elif map[f"{next_over},{next_down}"] == "O":
        #print("pushing boxes")

        o = robotOver
        d = robotDown
        o2 = o
        d2 = d

        cur =  map[f"{o2},{d2}"]
        stop = False
        while stop == False:
            o2 = o2 + over_adj
            d2 = d2 + down_adj
            cur =  map[f"{o2},{d2}"]
            if cur == "." or cur == "#":
                stop = True
        #print( cur, o2, d2 )
        if cur == ".":
                #teleport the box (hint from reddit user)
                map[f"{o2},{d2}"] = "O"

                map[f"{o},{d}"] = "."

                o = o + over_adj
                d = d + down_adj
                map[f"{o},{d}"] = "@"
                robotOver = o
                robotDown = d
    else:
        print("*** error ***")

    #print(f"robot at {robotOver}, {robotDown}")
    #print(m)
    #display(map)
    
print( "Part 1: ", gpsCount( map ) )  #1467421 low
print()
#print( len(moves) )
#display(map)

