import re
import itertools

yes = 0
no = 0

file = open("AOC_2024/day19/day19t0.txt", "r")

patterns = file.readline().strip().split(", ")
print(patterns)
print()

junk = file.readline()

count = 0
data = file.readline().strip()
while data:
    count += 1
    
    print()
    
    print( count, data )

    options = [data]
    found = False

    while len(options) > 0 and found == False:
        print( len(options))
        result = []
        possible = 0

        i = 0
        while i < len(options) and found == False:
        #for option in options:
            option = options[i]

            # Check each pattern
            j = 0
            while j < len(patterns):
            #for p in patterns:
                p = patterns[j]

                regex = re.compile("^" + p)
                if regex.match(option):
                    #print(p)
                    next_option = option[len(p):]
                    if next_option == "":
                        #print( "found")
                        found = True
                        break
                    else:
                        result.append(next_option)

                j += 1

            i += 1

        #print( "results:", result )
        options = result.copy()

    if found:
        print("OK", data)
        yes += 1
    else:
        print("Nope", data)
        no += 1
    #next one
    data = file.readline().strip()
    
print()
print("yes", yes)
print("no", no)

