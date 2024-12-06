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


def find_middle_sum(rules, updates):
    correct_updates = []
    middle_sum = 0

    for update in updates:
        if is_update_correct(rules, update):
            correct_updates.append(update)
            # Find the middle page number
            middle_page = update[len(update) // 2]
            middle_sum += middle_page

    return middle_sum, correct_updates


# Main execution
file_path = 'AOC_2024/day5/day5.txt'  # Replace with your file path
rules, updates = parse_input(file_path)

# Determine the sum of middle page numbers for correctly-ordered updates
middle_sum, correct_updates = find_middle_sum(rules, updates)

print(f"Sum of middle page numbers from correctly-ordered updates: {middle_sum}")
print("Correctly-ordered updates:")
for update in correct_updates:
    print(update)
