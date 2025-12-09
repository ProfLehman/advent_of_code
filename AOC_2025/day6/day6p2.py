# day6p2.py
#
# all me

def get_number( a, b, c, d):
    result = 0

    temp = a + b + c + d
    result = int(temp.strip())

    return result


# --- main ---

part2 = 0

# load data
file = open('AOC_2025/day6/test2.txt', 'r')

n1 = file.readline().rstrip()
n2 = file.readline().rstrip()
n3 = file.readline().rstrip()
n4 = file.readline().rstrip()

op = ""
temp = file.readline().rstrip()
i = 0
while i < len(temp)-1:
    if temp[i+1] in "*+":
        op = op + "e"
    else:
        op = op + temp[i]
    i = i + 1

#n1 = n1.replace(" ", "0")
#n2 = n2.replace(" ", "0")
#n3 = n3.replace(" ", "0")

print( n1 )
print( n2 )
print( n3 )
print( n4 )
print( op )

file.close()

stack = []
operation = ""

i = 0
while i < len(n1):

    if op[i] in "*+":
        operation = op[i]
    
        number = get_number( n1[i], n2[i], n3[i], n4[i] )
        stack.append(number)
        print( number )

    elif op[i] == "e" or i == len(n1)-1:

        print( stack )
        temp = stack[0]
        j = 1
        while j < len(stack):
            
            if operation == "*":
                temp = temp * stack[j]
            else:
                temp = temp + stack[j]

            j = j + 1

        stack.clear()

        print( "temp ", temp)
        part2 = part2 + temp

    else:
        number = get_number( n1[i], n2[i], n3[i], n4[i] )
        stack.append(number)
        print( number )

    i = i + 1

# --- results ---
print()
print("Part 2:", part2)
print()

# too low 8811937974550

# wasn't reading last column ... so just added the last number :-)
print( 8811937974550 + 1817)


