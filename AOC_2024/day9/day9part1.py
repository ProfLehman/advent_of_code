# --- Load Data ---
file = open('AOC_2024/day9/day9t.txt', 'r')

data = file.readline()

#print( data )
print( "data length: ", len(data) )

#--- Part I. ---
checkSum = 0

totalFiles = 0
totalSpace = 0

disk = []
id = 0
i = 0
while i < len(data):
    if i == 0 or i % 2 == 0:
        files = int(data[i])
        totalFiles += files
        for _ in range(0,files):
            disk.append(id)
        id += 1
    else:
        spaces = int(data[i])
        totalSpace += int(data[i])
        for _ in range(0,spaces):
            disk.append(-1)
    i += 1
    
print("00...111...2...333.44.5555.6666.777.888899")
print( disk )

print( "total files:", totalFiles)
print( "total space:", totalSpace)
print( "total disk:", len(disk))
print()

i = 0
j = len(disk)-1

while i < j:

    while disk[i] != -1 and i < j:
        i = i + 1
        #print("i =", i)

    while disk[j] == -1 and i < j:
        j = j - 1
        #print("j =", j)

    if i < j:
        disk[i] = disk[j]
        disk[j] = -1
        j = j-1

#print( i, j)
print("0099811188827773336446555566..............")
print( disk )
print( len(disk) )

checkSum = 0
i = 0
while i < len(disk):
    if disk[i] != -1:
        checkSum = checkSum + (i * int(disk[i]))
    i += 1

print("Part 1.", checkSum) #6323641412437 correct!
