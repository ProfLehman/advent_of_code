import re

def lowCost( a_x, a_y, b_x, b_y, p_x, p_y):
    
    found = False
    cost = -1

    for a in range(0,101):
        for b in range(0,101):
            if a * a_x  + b * b_x == p_x:
                if a * a_y  + b * b_y == p_y:
                    temp_cost = a * 3 + b
                    if found == False:
                        cost = temp_cost
                    elif temp_cost < cost:
                        cost = temp_cost
                    found = True    

    if not found:
        print("*** Not Found ***")
    
    return cost


# --- Load Data ------------------------------------------------------------------
file = open('AOC_2024/day13/day13.txt', 'r')
# --------------------------------------------------------------------------------
# $3 for a, $1 fo b
# 

part1 = 0 #cost to win prize


# Pattern to match positive or negative integers after + or =
pattern = r'[\+\=](\d+)'

data = file.readlines()
i = 0
while i < len(data):
    data[i] = data[i].strip()

    # Find all matches in the line
    temp = re.findall(pattern, data[i].strip())
    a_x = int(temp[0])
    a_y = int(temp[1])
    
    temp = re.findall(pattern, data[i+1].strip())
    b_x = int(temp[0])
    b_y = int(temp[1])

    temp = re.findall(pattern, data[i+2].strip())
    p_x = int(temp[0])
    p_y = int(temp[1])

    print( a_x, a_y, b_x, b_y, p_x, p_y)

    cost = lowCost( a_x, a_y, b_x, b_y, p_x, p_y)
    print( cost )
    print()

    if cost != -1:
        part1 = part1 + cost

    # next puzzle
    i = i + 4
    
    
print( "Part I: ", part1 ) #27157 first go :-)



