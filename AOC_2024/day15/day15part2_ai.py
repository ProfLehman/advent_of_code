def gpsCount(map, width, height):
    count = 0
    for down in range(height):
        for over in range(width):
            if map.get(f"{over},{down}") == "[":
                # Calculate GPS coordinate for the left edge of the box
                gps = (down + 1) * 100 + (over + 1)
                count += gps
    return count

def display(map, width, height):
    for down in range(height):
        for over in range(width):
            print(map.get(f"{over},{down}", " "), end="")
        print()
    print()

def rescale_map(original_map, original_width, original_height):
    new_map = {}
    new_width = original_width * 2
    for down in range(original_height):
        for over in range(original_width):
            tile = original_map[f"{over},{down}"]
            new_over = over * 2
            if tile == "#":
                new_map[f"{new_over},{down}"] = "#"
                new_map[f"{new_over + 1},{down}"] = "#"
            elif tile == "O":
                new_map[f"{new_over},{down}"] = "["
                new_map[f"{new_over + 1},{down}"] = "]"
            elif tile == ".":
                new_map[f"{new_over},{down}"] = "."
                new_map[f"{new_over + 1},{down}"] = "."
            elif tile == "@":
                new_map[f"{new_over},{down}"] = "@"
                new_map[f"{new_over + 1},{down}"] = "."
    return new_map, new_width

# --- Load Data ---
file_content = """
#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######
<vv<<^^<<^^
"""
lines = file_content.strip().split("\n")

# Parse map
original_map = {}
moves = []
original_width = len(lines[0])
original_height = len(lines)
robotOver = -1
robotDown = -1

for down, line in enumerate(lines):
    if line[0] in "<>^v":
        moves.extend(line.strip())
        break
    for over, char in enumerate(line):
        original_map[f"{over},{down}"] = char
        if char == "@":
            robotOver, robotDown = over, down

print(f"Original width: {original_width}, Original height: {original_height}")
display(original_map, original_width, original_height)

# Rescale map
new_map, new_width = rescale_map(original_map, original_width, original_height)
new_height = original_height

print("Rescaled map:")
display(new_map, new_width, new_height)

# --- Process Moves ---
for count, m in enumerate(moves, start=1):
    move_symbols = "><^v"
    over_options = [1, -1, 0, 0]
    down_options = [0, 0, -1, 1]
    position = move_symbols.find(m)
    if position == -1:
        continue
    over_adj = over_options[position]
    down_adj = down_options[position]

    next_over = robotOver + over_adj
    next_down = robotDown + down_adj

    # Boundary check
    if next_over < 0 or next_over >= new_width or next_down < 0 or next_down >= new_height:
        continue

    if new_map.get(f"{next_over},{next_down}") == "#":
        continue
    elif new_map.get(f"{next_over},{next_down}") == ".":
        new_map[f"{robotOver},{robotDown}"] = "."
        new_map[f"{next_over},{next_down}"] = "@"
        robotOver, robotDown = next_over, next_down
    elif new_map.get(f"{next_over},{next_down}") == "[":
        push_over = next_over + over_adj
        push_down = next_down + down_adj

        # Boundary check for pushing
        if push_over < 0 or push_over >= new_width or push_down < 0 or push_down >= new_height:
            continue

        if new_map.get(f"{push_over},{push_down}") == ".":
            new_map[f"{push_over},{push_down}"] = "["
            new_map[f"{push_over + 1},{push_down}"] = "]"
            new_map[f"{next_over},{next_down}"] = "@"
            new_map[f"{next_over + 1},{next_down}"] = "."
            new_map[f"{robotOver},{robotDown}"] = "."
            robotOver, robotDown = next_over, next_down

    print(f"After move {count} ({m}):")
    display(new_map, new_width, new_height)

# Calculate GPS coordinates sum
result = gpsCount(new_map, new_width, new_height)
print("Part 2: Sum of GPS coordinates =", result)
