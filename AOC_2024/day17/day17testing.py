
def octalToDecimal(n): 
  
    num = n 
    dec_value = 0
  
    # Initializing base value 
    # to 1, i.e 8^0 
    base = 1
  
    temp = num 
    while (temp): 
  
        # Extracting last digit 
        last_digit = temp % 10
        temp = int(temp / 10) 
  
        # Multiplying last digit 
        # with appropriate base 
        # value and adding it 
        # to dec_value 
        dec_value += last_digit * base 
  
        base = base * 8
  
    return dec_value

max = -1

def runCode(A):
    global max
    result = ""
    B = 0
    C = 0
    expected = [2,4,1,7,7,5,0,3,1,7,4,1,5,5,3,0]
    ei = 0
    
    stop = False
    while stop == False:
        #print( A, B, C)
        B = A % 8
        B = B ^ 7
        C = int( A / 2**B )
        A = int( A / 8 )
        B = B ^ 7
        B = B ^ C
        output = str(B % 8)
        result += output + "," 
        
        if A == 0:
            stop = True
            
    return result[:-1]

def runCodeAI(A):
    global max
    parts = []
    B = 0
    C = 0
    expected = [2, 4, 1, 7, 7, 5, 0, 3, 1, 7, 4, 1, 5, 5, 3, 0]
    ei = 0
    
    while True:
        B = (A % 8) ^ 7
        C = A >> B  # Replaces int(A / 2**B) with a bitwise shift
        A >>= 3     # Replaces int(A / 8) with a bitwise shift
        
        B = (B ^ 7) ^ (C % 8)
        output = str(B)
        
        if output != str(expected[ei]):
            if len(output) > max:
                max = len(output)
                print("                            ", max)
            break
        
        parts.append(output)
        
        if A == 0:
            break
        
        ei += 1  # Increment the index for expected list
    
    return ",".join(parts)


#--- test ---

#A = 64723093456 # 7,5,0,3,1,7,4,1,5,5,3,0
#A = 517784747648
#A = 517785796224

found = False
count = 0
testData = [3,2,4,1,7,7,5,0,3,1,7,4,1,5,5,3,0]

A = 265652340990877
while True:
    test = runCode(A)
    if test == "2,4,1,7,7,5,0,3,1,7,4,1,5,5,3,0":
        print("found, A=", A )
    
    A = A - 1
      
#print( runCodeAI(64012472) ) #1,0,2,0,5,7,2,1,3
         
#print( runCode(265652340990877) ) #265652340990877 - too high
    

# tried this approach from Reddit, but could not get last digits,
# moved to Z3 see othe file
#     
"""
My solution is based on an analysis of the program itself.
each iteration outputs only based on the lowest 3 bits,
and divides a by 8 after each iteration so the lowest 3 bits
are thrown out. thus each iteration is completely independent.
so i loop, starting with a=0, incrementing by one each time
until i find an a that outputs the last instruction.
then i multiply it by 8 and iterate starting with that value
until i get the last two instructions. i repeat this process
until i get the entire program.
"""    

    
    
    
