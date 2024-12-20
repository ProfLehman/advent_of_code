def count_ways(data, patterns):
    n = len(data)
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: There's 1 way to construct an empty string.

    for i in range(1, n + 1):
        for pattern in patterns:
            plen = len(pattern)
            # Check if the pattern matches the substring ending at i
            if i >= plen and data[i - plen:i] == pattern:
                dp[i] += dp[i - plen]  # Add the ways from the previous valid state

    print( "dp", dp )
    return dp[n]

# Example usage
with open("AOC_2024/day19/day19t1.txt", "r") as file:
    patterns = file.readline().strip().split(", ")
    print("Patterns:", patterns)
    print()
    file.readline()  # Skip junk line
    strings = file.readlines()

total_ways = 0
for count, data in enumerate(strings, start=1):
    data = data.strip()
    print(f"{count}. {data}")

    ways = count_ways(data, patterns)
    if ways > 0:
        print(f"OK ({ways} ways): {data}")
    else:
        print(f"Nope: {data}")

    total_ways += ways
    print()
    
# Print total
print()
print("Total number of ways:", total_ways)
