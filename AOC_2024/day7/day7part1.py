import math

# --- Load Data ---
file = open('AOC_2024/day7/day7.txt', 'r')

part1 = 0

data = file.readlines()
i = 0
while i < len(data):

    #extract annswer and numbers
    data[i] = data[i].strip()
    colon = data[i].find(":")
    answer = int( data[i][:colon] )
    numbers = data[i][colon+2:].split(" ")

    # convert to ints    
    j = 0
    while j < len(numbers):
        numbers[j] = int( numbers[j] )
        j += 1

    numOps = len(numbers) - 1
    combos = 2**numOps
    binaryWidth = int(math.log2(combos))

    #print( f"{answer} {numbers} - #numOps {numOps} - #combos {combos} - binaryWitdh {binaryWidth}" )
    
    #print( f"{answer} {numbers}")
    j = 0
    found = False
    while j < combos and found == False:

        opsMask = f"00000000000000000000{j:b}"[-binaryWidth:]
        #print( opsMask )
        
        numbersIndex = 1 
        tempAnswer = numbers[ 0 ]

        opsMaskIndex = 0
        while opsMaskIndex < len(opsMask):
            if opsMask[opsMaskIndex] == "0":
                tempAnswer = tempAnswer + numbers[numbersIndex]
            else:
                tempAnswer = tempAnswer * numbers[numbersIndex]
            numbersIndex += 1
            opsMaskIndex += 1

        if tempAnswer == answer:
            found = True
            print("found ", opsMask)
            part1 += answer

        j += 1
        #end loop checking ops combinations
    #print()
    i = i + 1
    #end loop reading data

#print( data )
print( "Part 1:", part1 )