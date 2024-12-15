import re
import pulp as pl

def lowCost( a_x, a_y, b_x, b_y, p_x, p_y):
    
    found = False
    cost = -1

    for a in range(0,101):
        for b in range(0,101):
            if a * a_x  + b * b_x == p_x:
                if a * a_y  + b * b_y == p_y:
                    temp_cost = a * 3 + b
                    if found == False:
                        cost = temp_cost
                    elif temp_cost < cost:
                        cost = temp_cost
                    found = True    

    if not found:
        print("*** Not Found ***")
    
    return cost

def lowCost2( a_x, a_y, b_x, b_y, p_x, p_y):
    
    coefficients = {
        'A': [a_x, a_y],
        'B': [b_x, b_y]
    }
    prizes = [p_x, p_y]

    found = False
    cost = -1

    # Define the problem
    problem = pl.LpProblem("Minimize_Cost", pl.LpMinimize)

    # Define the variables
    A = pl.LpVariable('A', lowBound=0, cat='Integer')
    B = pl.LpVariable('B', lowBound=0, cat='Integer')

    # Objective function
    problem += 3 * A + B, "TotalCost"

    # Build and print equations for verification
    equation1_str = f"{coefficients['A'][0]}*A + {coefficients['B'][0]}*B = {prizes[0]}"
    equation2_str = f"{coefficients['A'][1]}*A + {coefficients['B'][1]}*B = {prizes[1]}"

    # Print the equations
    print("Equation 1:", equation1_str)
    print("Equation 2:", equation2_str)

    # Add constraints based on extracted coefficients and prizes
    problem += coefficients['A'][0] * A + coefficients['B'][0] * B == prizes[0], "Equation_X"
    problem += coefficients['A'][1] * A + coefficients['B'][1] * B == prizes[1], "Equation_Y"

    # Solve the problem
    status = problem.solve(pl.SCIP_PY())

    # Output the results
    if status == pl.LpStatusOptimal:
        print(f"Optimal values: A = {pl.value(A)}, B = {pl.value(B)}")
        print(f"Minimum cost: {pl.value(problem.objective)}")
        found = True
        cost = int(pl.value(problem.objective))
    else:
        print("No optimal solution could be found.")

    if not found:
        print("*** Not Found ***")
    
    return cost


# --- Load Data ------------------------------------------------------------------
file = open('AOC_2024/day13/day13.txt', 'r')
# --------------------------------------------------------------------------------
# $3 for a, $1 fo b
# 

part1 = 0
part2 = 0 #cost to win prize


# Pattern to match positive or negative integers after + or =
pattern = r'[\+\=](\d+)'

data = file.readlines()
i = 0
while i < len(data):
    data[i] = data[i].strip()

    # Find all matches in the line
    temp = re.findall(pattern, data[i].strip())
    a_x = int(temp[0])
    a_y = int(temp[1])
    
    temp = re.findall(pattern, data[i+1].strip())
    b_x = int(temp[0])
    b_y = int(temp[1])

    temp = re.findall(pattern, data[i+2].strip())
    p_x = int(temp[0])
    p_y = int(temp[1])

    print( a_x, a_y, b_x, b_y, p_x, p_y)

    cost = lowCost( a_x, a_y, b_x, b_y, p_x, p_y)
    if cost != -1:
        part1 = part1 + cost
    print( "p1 cost", cost )
  
    cost2 = lowCost2( a_x, a_y, b_x, b_y, p_x+10000000000000, p_y+10000000000000)
    if cost2 != -1:
        part2 = part2 + cost2
    print( "p2 cost", cost2 )
    


    # next puzzle
    i = i + 4
    
    
print( " Part I: ", part1 ) 
print( "Part II: ", part2 ) # 144913377701805 too high


