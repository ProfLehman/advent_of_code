from z3 import Solver
from z3 import BitVec
from z3 import sat

# Initialize the solver
solver = Solver()

# Define the variable for A as a 32-bit integer (you might need to adjust the bit-width)
A = BitVec('A', 51)

# The expected output sequence
#expected = [2, 4, 1, 7, 7, 5, 0, 3, 1, 7, 4, 1, 5, 5, 3, 0]

expected = [2,4,1,7,7,5,0,3,1,7,4,1, 5, 5, 3, 0]

# The constraints based on the function logic
def add_constraints(A, expected):
    B = 0
    C = 0
    a = A  # We will manipulate 'a' instead of 'A' directly
    for ei, exp in enumerate(expected):
        # Calculate B and C as per the function
        B = (a % 8) ^ 7
        C = a >> B
        a = a >> 3
        # Calculate final B and compare to expected
        final_B = (B ^ 7) ^ C % 8
        # Add constraint that the computed B must match the expected value
        solver.add(final_B % 8 == exp)

        # Check if we should stop
        if ei == len(expected) - 1:  # On the last expected output, ensure 'a' is zero
            solver.add(a == 0)

# Add constraints to the solver
add_constraints(A, expected)

# Check if the solver can find a solution
if solver.check() == sat:
    m = solver.model()
    print("Found A =", m[A])
else:
    print("No solution found")
