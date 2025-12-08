# day6.py
#
# all me

# --- main ---

part1 = 0
part2 = 0

# load data
file = open('AOC_2025/day6/test1.txt', 'r')

temp = file.readline().strip().split()
n1 = []
for n in temp:
    n1.append( int(n) )

temp = file.readline().strip().split()
n2 = []
for n in temp:
    n2.append( int(n) )

temp = file.readline().strip().split()
n3 = []
for n in temp:
    n3.append( int(n) )

#temp = file.readline().strip().split()
#n4 = []
#for n in temp:
#    n4.append( int(n) )

op = file.readline().strip().split()

print( n1 )
print()
print( n2 )
print()
print( n3 )
print()
#print( n4 )
#print()
print( op )

file.close()

# part1
for i in range(0, len(n1)):

    if op[i] == "*":
        part1 = part1 +  (n1[i] * n2[i] * n3[i]) # * n4[i])
    elif op[i] == "+":
        part1 = part1 +  (n1[i] + n2[i] + n3[i]) # + n4[i])
    else:
        print("*** error: invalid operator ***", op[i])

# --- results ---
print()
print("Part 1:", part1)
print("Part 2:", part2)
print()

# too low 2354142