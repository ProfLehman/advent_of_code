# day 17
#
#Register A: 729
#Register B: 0
#Register C: 0
#Program: 0,1,5,4,3,0

#A = 729
#B = 0
#C = 0
#P = [0,1,5,4,3,0]



#A = 0
#B = 2024
#C = 43690
#P = [4,0]

"""
Combo Operands
0, 1, 2, 3 - literal values
5 - A, 6 - B, 7 - C
"""

def codeRun( A, B, C, P ):
    
    display = []
    stop = False
    di = 0 #display index
    
    I = 0
    while I < len(P) and stop == False:
        
        instr = P[I]
        op = P[I+1]
        
        #print()
        #print( f"instr:{instr}  op:{op}" )
        #print( f"A:{A}, B:{B}, C:{C}, I:{I}" )
        
        if instr == 0:
            #print("0 adv")
            if A == 0:
                print("*** error 0 adv divide by zero ***")
            elif op >= 0 and op <= 3:
                A = int( A / (2**op) )
            elif op == 4:
                A = int( A / (2**A) )
            elif op == 5:
                A = int( A / (2**B) )
            elif op == 6:
                A = int( A / (2**C) )
            else:
                print("*** error 0 adv ***")
            I += 2
            
        elif instr == 1:
            #print("1 bxl")
            B = B ^ op
            I += 2
            
        elif instr == 2:
            #print("2 bst")
            if op >= 0 and op <= 3:
                B = op % 8
            elif op == 4:
                B = A % 8
            elif op == 5:
                B = B % 8
            elif op == 6:
                B = C % 8
            else:
                print("*** error 2 bst ***")
            I += 2
            
        elif instr == 3:
            #print("3 jnz")
            if A != 0:
                I = op
            else:
                I += 2
                
        elif instr == 4:
            #print("4 bxc")
            B = B ^ C
            I += 2
            
        elif instr == 5:
            #print("5 out")
            if op >= 0 and op <= 3:
                value = op % 8
            elif op == 4:
                value = A % 8 
            elif op == 5:
                value = B % 8 
            elif op == 6:
                value = C % 8 
            else:
                print("*** error 5 out ***")
            display.append(value)
            I += 2
            
            # part 2. check stops once display does not match - remove for part 1
            #if display[di] != P[di]:
            #    stop = True
                #print("Killed", len(display))
            #di += 1
            
        elif instr == 6:
            #print("6 bdv")
            if A == 0:
                print("*** error 0 bdv divide by zero ***")
            elif op >= 0 and op <= 3:
                B = int( A / (2**op) )
            elif op == 4:
                B = int( A / (2**A) )
            elif op == 5:
                B = int( A / (2**B) )
            elif op == 6:
                B = int( A / (2**C) )
            else:
                print("*** error 6 bdv ***")
            I += 2
            
        elif instr == 7:
            #print("7 cdv")
            if A == 0:
                print("*** error 0 bdv divide by zero ***")
            elif op >= 0 and op <= 3:
                C = int( A / (2**op) )
            elif op == 4:
                C = int( A / (2**A) )
            elif op == 5:
                C = int( A / (2**B) )
            elif op == 6:
                C = int( A / (2**C) )
            else:
                print("*** error 7 cdv ***")
            I += 2
            
        else:
            print("*** error invalid instruction ***")


    #print()
    #print("---- final ----")
    #print( f"instr:{instr}  op:{op}" )
    #print( f"A:{A}, B:{B}, C:{C}, I:{I}" )
        
    #print()
    #print( display )        
    part1 = ""
    for d in display:
        part1 += str(d) + ","
    #print( part1[:-1] ) #Part 1. 1,0,2,0,5,7,2,1,3
    return part1[:-1]

# --- main ---
#print( codeRun( 729, 0, 0, [0,1,5,4,3,0] ) ) #t1. 4,6,3,5,6,3,5,2,1,0
#print( codeRun( 64012472, 0, 0, [2,4,1,7,7,5,0,3,1,7,4,1,5,5,3,0] ) ) #Part 1. 1,0,2,0,5,7,2,1,3
print()

"""
A = 1
stop = False
while not stop:
    #print( "testing A = ", A )
    #if codeRun( A, 0, 0, [0,3,5,4,3,0] ) == "0,3,5,4,3,0":
    if codeRun( A, 0, 0, [2,4,1,7,7,5,0,3,1,7,4,1,5,5,3,0] ) == "2,4,1,7,7,5,0,3,1,7,4,1,5,5,3,0":
        print( "Found: A = ", A )
        stop = True
    A = A + 1
    if A % 1000000 == 0:
        print( f"A: {A:,}" )
"""
#for A in range(1000000000000, 1000001000000):
#    test = codeRun( A, 0, 0, [2,4,1,7,7,5,0,3,1,7,4,1,5,5,3,0] )
#    if len(test) >= 10:
#        print( A, test )

count = 0
p = [2,4,1,7,7,5,0,3,1,7,4,1,5,5,3,0]

r = 470
r = 3760
#r = 30080
ns = []
ts = [1011298328, 1011300376, 1013383256, 1013395480]
for t in ts:
    r = t
    for A in range(r,r+9):
        count += 1
        temp = codeRun(A, 0, 0, p)
        if temp == "3,1,7,4,1,5,5,3,0":
            print(A, "=>", temp, f"{A:o}", A*8)
            ns.append(A*8)
        
print( ns[0:10] )



