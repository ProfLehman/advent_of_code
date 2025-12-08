# day6p2.py
#
# all me

# --- main ---

part2 = 0

# load data
file = open('AOC_2025/day6/test1.txt', 'r')

n1 = file.readline().rstrip()
n2 = file.readline().rstrip()
n3 = file.readline().rstrip()

op = ""
temp = file.readline().rstrip()
i = 0
while i < len(temp)-1:
    if temp[i+1] in "*+":
        op = op + "e"
    else:
        op = op + temp[i]
    i = i + 1

n1 = n1.replace(" ", "0")
n2 = n2.replace(" ", "0")
n3 = n3.replace(" ", "0")

print( n1 )
print( n2 )
print( n3 )
#print( n4 )
print( op )

file.close()

stack = []
operation = ""

i = 0
while i < len(n1):

    if op[i] in "*+":
        operation = op[i]
    
        number = int(n1[i]) * 100 + int(n2[i]) * 10 + int(n3[i])
        print( number, type(number) )
        stack.append(number)

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
        number = int(n1[i]) * 100 + int(n2[i]) * 10 + int(n3[i])
        stack.append(number)

    i = i + 1

# --- results ---
print()
print("Part 2:", part2)
print()
