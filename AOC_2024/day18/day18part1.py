# --- Load Data ------------------------------------------------------------------
file_path = "AOC_2024/day18/day18t2.txt"
# --------------------------------------------------------------------------------

def display(m, w, h):
    down = 0
    while down < h:
        over = 0
        while over < w:
            key = f"{over},{down}"
            if key in map:
                print("#", end="")
            else:
                print(".", end="")
            over += 1
        print()
        down += 1
    print()
    

map = {}
width = 7  #0 to 6, 0 to 70
height = 7


# Open the file and read the contents
with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()
        if line:  # Check if line is not empty
            over, down = line.split(',')           
            map[f"{int(over)},{int(down)}"] = "#"

# Now over_down_values contains all the pairs from the file
print(map)
display( map, width, height)
