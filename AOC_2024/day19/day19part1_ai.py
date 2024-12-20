import re

# Read patterns and input strings from file
with open("AOC_2024/day19/day19t0.txt", "r") as file:
    patterns = file.readline().strip().split(", ")
    print("Patterns:", patterns)
    print()
    file.readline()  # Skip junk line
    strings = file.readlines()

# Compile regex patterns for efficiency
regex_patterns = [re.compile("^" + pattern) for pattern in patterns]

yes, no = 0, 0

# Function to check if a string can be constructed using the patterns
def can_construct(data, patterns):
    n = len(data)
    dp = [False] * (n + 1)
    dp[0] = True  # Base case: Empty string is always valid

    for i in range(1, n + 1):
        for pattern in patterns:
            plen = len(pattern)
            if i >= plen and dp[i - plen] and data[i - plen:i] == pattern:
                dp[i] = True
                break

    return dp[n]

# Process each string
for count, data in enumerate(strings, start=1):
    data = data.strip()
    print(f"{count}. {data}")

    if can_construct(data, patterns):
        print("OK", data)
        yes += 1
    else:
        print("Nope", data)
        no += 1

# Print results
print()
print("yes", yes)
print("no", no)
