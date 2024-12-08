from itertools import product

# eval numbers
def evalAddMultList( temp ):
    value = int(temp[0])
    i = 1
    while i < len(temp):
        if temp[i] == "+":
            value = value + int(temp[i+1])
        else:
            value = value * int(temp[i+1])
        i = i + 2
    return value

def mergeNumbersOps( tempN, tempO ):
    temp = []
    indexN = 0
    indexO = 0
    while indexN < len(tempN)-1:
        temp.append( tempN[indexN ] )
        temp.append( tempO[indexO ] )
        indexN += 1
        indexO += 1
    temp.append( tempN[indexN ] )
    return temp

def allCombos(a, n, ops):

    result = 0

    # Number of columns
    num_columns = len(n)-1

    # Generate all combinations
    combinations = product(ops, repeat=num_columns)

    # Convert and display each combination as a string
    for combo in combinations:
        #print(''.join(combo))
        #print( combo )
        tempList = mergeNumbersOps(n, combo)

        # fix || lists
        #print( tempList )
        mystack = [tempList[0]]
        i = 1
        while i < len(tempList):
            if tempList[i] == "|":
                top = mystack.pop()
                mystack.append(top+tempList[i+1])
                i += 2
            elif tempList[i] == "+":
                top = mystack.pop()
                mystack.append( str(int(top)+int(tempList[i+1])) )  
                i += 2
            elif tempList[i] == "*":
                top = mystack.pop()
                mystack.append( str(int(top)*int(tempList[i+1])) )  
                i += 2
            else:
                print("Error processing stack")

        #print( mystack )
        #print()

        if int(mystack[0]) == a:
            return a

    return 0

def checkPart1( a, n ):
    return allCombos( a, n, ["+", "*"] )

def checkPart2( a, n ):    
    return allCombos( a, n, ["+", "*", "|"] )

#print( evalAddMultList( ["10","*","30","+","40"] ) )
#allCombos( ["10","20","30"],["+", "*"] )
#allCombos( ["10","20","30"],["+", "*", "||"] )
#print( checkPart1( 600, ["10","30","2"] ) )

# --- Load Data ---
file = open('AOC_2024/day7/day7.txt', 'r')

part1 = 0
part2 = 0

data = file.readlines()
i = 0
while i < len(data):

    #extract annswer and numbers
    data[i] = data[i].strip()
    colon = data[i].find(":")
    answer = int( data[i][:colon] )
    numbers = data[i][colon+2:].split(" ")

    part1 += checkPart1( answer, numbers)
    part2 += checkPart2( answer, numbers)

    i = i + 1
    #end loop reading data

#print( data )
print( "Part 1:", part1 )
print( "Part 2:", part2 )

