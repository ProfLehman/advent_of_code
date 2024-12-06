from collections import defaultdict, deque

def parse_input(file_path):
    rules = []
    updates = []
    reading_rules = True

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                reading_rules = False
                continue

            if reading_rules:
                if '|' in line:
                    rules.append(tuple(map(int, line.split('|'))))
            else:
                updates.append(list(map(int, line.split(','))))

    return rules, updates


def is_update_correct(rules, update):
    # Create a mapping of page positions for the current update
    position = {page: idx for idx, page in enumerate(update)}
    
    for x, y in rules:
        # Check if both x and y are in the update
        if x in position and y in position:
            # Ensure x appears before y
            if position[x] > position[y]:
                return False
    return True


def sort_update(rules, update):
    # Create a graph and an in-degree counter for topological sorting
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    update_set = set(update)

    for x, y in rules:
        if x in update_set and y in update_set:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0

    # Perform topological sorting
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_update = []

    while queue:
        node = queue.popleft()
        sorted_update.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_update


def find_middle_sum(rules, updates):
    correct_updates = []
    incorrect_updates = []
    middle_sum_correct = 0
    middle_sum_incorrect = 0

    for update in updates:
        if is_update_correct(rules, update):
            correct_updates.append(update)
            middle_sum_correct += update[len(update) // 2]
        else:
            sorted_update = sort_update(rules, update)
            incorrect_updates.append(sorted_update)
            middle_sum_incorrect += sorted_update[len(sorted_update) // 2]

    return middle_sum_correct, middle_sum_incorrect, correct_updates, incorrect_updates


# Main execution
file_path = 'AOC_2024/day5/day5.txt'  # Replace with your file path
rules, updates = parse_input(file_path)

# Calculate sums and get sorted updates
middle_sum_correct, middle_sum_incorrect, correct_updates, incorrect_updates = find_middle_sum(rules, updates)

print(f"Sum of middle page numbers from correctly-ordered updates: {middle_sum_correct}")
print("Correctly-ordered updates:")
for update in correct_updates:
    print(update)

print(f"\nSum of middle page numbers after fixing incorrectly-ordered updates: {middle_sum_incorrect}")
print("Fixed incorrectly-ordered updates:")
for update in incorrect_updates:
    print(update)
