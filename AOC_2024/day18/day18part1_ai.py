import networkx as nx

def display(wl, pt, w, h):
    down = 0
    while down < h:
        over = 0
        while over < w:
            key = (over, down)
            if (over, down) in wl:
                print("#", end="")
            elif (over, down) in pt:
                print("O", end="")
            else:
                print(".", end="")
            over += 1
        print()
        down += 1
    print()

def read_wall_positions(file_path):
    walls = set()
    count = 0
    over = -1
    down = -1
    file = open(file_path, 'r')
    data = file.readlines()
    d = 0
    while d < len(data):
        line = data[d].strip()
        if line:
            over, down = map(int, line.split(','))
            walls.add((over, down))

        count = count + 1
        print( count, over, down)
        if count == 3046:
            print( over, down)
            break;
        d += 1

    return walls

def create_graph_from_walls(walls, width, height):
    G = nx.Graph()
    # Add edges where there are no walls
    for i in range(height):
        for j in range(width):
            if (i, j) not in walls:
                # Check adjacent cells (down and right only to avoid duplication)
                if i < height - 1 and (i + 1, j) not in walls:
                    G.add_edge((i, j), (i + 1, j))
                if j < width - 1 and (i, j + 1) not in walls:
                    G.add_edge((i, j), (i, j + 1))
    return G

def find_shortest_path(G, start, end):
    try:
        path = nx.shortest_path(G, source=start, target=end)
        return path
    except nx.NetworkXNoPath:
        return "No path found"

# Example usage
file_path = "AOC_2024/day18/day18t0.txt"
walls = read_wall_positions(file_path)

# Define the grid size; you might want to adjust this based on your specific requirements
grid_width = 71  # max x-coordinate + 1
grid_height = 71 # max y-coordinate + 1

G = create_graph_from_walls(walls, grid_width, grid_height)
path = find_shortest_path(G, (0, 0), (grid_height - 1, grid_width - 1))
print("Shortest path:", path)
print("Shortest path steps:", len(path)-1) #part 1: 310
#display( walls, path, grid_width, grid_height)