
stones = [0, 27, 5409930, 828979, 4471, 3, 68524, 170] #my data

stones = [125, 17]
#stones = [0]

i = 1
while i <= 50:

    new_stones = []
    
    for s in stones:
        if s == 0:
            new_stones.append(1)

        elif len(str(s)) % 2 == 0:
            temp = str(s)
            half = len(temp)//2
            new_stones.append( int(temp[:half]) )
            new_stones.append( int(temp[half:]) )
        else:
            new_stones.append( s * 2024)
   
    stones = new_stones
    print( i, len(stones) )

    i = i + 1






