def printN( c, n):
    while n > 0:
        #print(f"{c}", end="")
        if c == ".":
            disk.append(-1)
        else:
            disk.append(c)
        n = n - 1

def display(f):

    i = 0
    while i < len(data):
        fs_data = fs[i]
        
        if len(fs_data) > 1:
            j = 1
            while j < len(fs_data):
                printN( fs_data[j], fs_data[j+1] )
                j += 2             
        
        printN( ".", fs_data[0])
        
        i = i + 1
    print()

# --- Load Data ---
file = open('AOC_2024/day9/day9.txt', 'r')

data = file.readline()

#print( data )
print( "data length: ", len(data) )

#--- Part I. ---

# bulid fs
fs = {}
id = 0
i = 0
while i < len(data):
    if i == 0 or i % 2 == 0:
        fs[i] = [0, id, int(data[i])]
        id += 1
    else:
        fs[i] = [int(data[i])]

    i += 1

# display fs
#display(fs)

# try to defrag files

# get file to place
r = len(data)-1

while r > 1:
    #print()
    #print( "searching for open spot for", fs[r] )
    f_size = fs[r][2]
    f_id = fs[r][1]
    #print( "file to place", f_id, f_size)

    # look for place to move file
    i = 1
    while i < r and fs[i][0] < f_size:
        #print( i )
        i = i + 1

    # if possible move r
    if i < r:
        #print(f"moving {r} to {i}")
        free_blocks = fs[i][0]
        #print(free_blocks, "free at", i)
        free_blocks = free_blocks - f_size
        new_block = [free_blocks]
        j = 1
        while j < len(fs[i]):
            new_block.append( fs[i][j])
            j += 1
        new_block.append( f_id)
        new_block.append( f_size ) 
        fs[i] = new_block
        fs[r] = [f_size] #mark previous spot with spaces
    #else:
        #print("no spot found")
    r = r - 2

disk = []
display(fs)
#print( disk )
print( len(disk) )

checkSum = 0
i = 0
while i < len(disk):
    if disk[i] != -1:
        checkSum = checkSum + (i * int(disk[i]))
    i += 1

print("Part 2.", checkSum) #6351801932670 .. oh yeah!


