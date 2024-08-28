# CS_3308 Gaussian Elimination using backwards substitution
# Group members: Leonel Kachie, Alessio Naji-Sepasgozar, Minh Anh Thai

import math 

def gausselim(A):                                           # Gaussian Elimination Function that takes a matrix array as an argument
    n = len(A)                                              # Sets n to the number of rows in array
                                                            
    for i in range(n-1):                                    # Forward elimination loop
                                                           
        p = -1                                              # Set pivot to default - value, p = row index
        for k in range(i, n):                               # Loop through rows to Find first pivot
            if A[k][i] != 0:                                # Checks if entry is non-zero
                p = k                                       # Updates pivot value if entry is non-zero
                break                                       # breaks nested loop 

        if p == -1:                                         # Checks if rows do not have a non zero entry (no unique solution)
            print('No unique solution exists')              # Print statement
            return None

        if p != i:                                          # Checks if pivot row is in the current row
            A[i], A[p] = A[p], A[i]                         # Swaps rows if pivot is not in current row                  

    
        for j in range(i+1, n):                             # Elimination loop
            if A[i][i] == 0:                                # Checks for 0 division 
                continue                                    # Continues loop 
            Mji = A[j][i] / A[i][i]                         # Mji variable, multiplier to make ith entry 0 
            for k in range(i, n+1):                         
                A[j][k] = A[j][k] - Mji * A[i][k]           # Updates row 'j' with a value that substracts the MJI sum * row 'i'

    if A[n-1][n-1] == 0:                                    # Checks bottom right element, if 0, no unique solutions is printed
        print("No unique solution exists")
        return None
                                
                                                            # Backwards Elimination steps
    x = [0.0] * n                                           # initializes a vector/matrix with zeroes 
    x[n-1] = A[n-1][n] / A[n-1][n-1]                        # Calculates value of last variable using last equation of augmented matrix

    for i in range(n-2, -1, -1):                                            # Backward substitution loop starting from 2nd to last to first row with backwards step size
        sum_ai = sum(A[i][j] * x[j] for j in range(i+1, n))                 # Calculates sum of known variables mulitplied by coefficients of matrix
        if A[i][i] == 0:                                                    # Checks for division by 0 
            print("No unique solution exists due to division by zero")
            return None
        x[i] = (A[i][n] - sum_ai) / A[i][i]                                 # Solve for unkown varables (x1, x2...)

    return x

A = [                                                                       # Augemented matrix from #8 (c)
    [math.pi, math.sqrt(2), -1, 1, 0],
    [math.e, -1, 1, 2, 1],
    [1, 1, -math.sqrt(3), 1, 2],
    [-1, -1, 1, -math.sqrt(5), 3]
]

print("Question 8.C \n")
solution = gausselim(A)                                                     # Pass matrix as argument                            

if solution:
    print("Solutions:")                                                    # If unique solution, print values
    print(f"X1 = {solution[0]}")                                            # X1 Value
    print(f"X2 = {solution[1]}")                                            # X2 Value
    print(f"X3 = {solution[2]}")                                            # X3 Value
    print(f"X4 = {solution[3]}\n")                                          # X4 Value


eq1 = math.pi * solution[0] + math.sqrt(2) * solution[1] - solution[2] + solution[3] # Test values by plugging solutions into original equations
eq2 = math.e * solution[0] - solution[1] + solution[2] + 2 * solution[3]
eq3 = solution[0] + solution[1] - math.sqrt(3) * solution[2] + solution[3]
eq4 = -solution[0] - solution[1] + solution[2] - math.sqrt(5) * solution[3]

print("Approximation of equation value using solutions found:", eq1, eq2, eq3, eq4, "\n")     # Check to see if original equations match with approxximations 


A2 = [                                                                              # Augemented matrix from #8 (d)
    [1, 1, -1, 1, -1, 2],
    [2, 2, 1, -1, 1, 4],
    [3, 1, -3, -2, 3, 8],
    [4, 1, -1, 4, -5, 16],
    [16, -1, 1, -1, -1, 32]
]

solution = gausselim(A2)
print("Question 8.D \n")
if solution:     
    print("Solutions:")                                                             # If unique solution, print values
    print(f"X1 = {solution[0]}")                                                    # X1 Value
    print(f"X2 = {solution[1]}")                                                    # X2 Value
    print(f"X3 = {solution[2]}")                                                    # X3 Value
    print(f"X4 = {solution[3]}")                                                    # X4 Value
    print(f"X5 = {solution[4]} \n")                                                 # X5 Value


eq1 = solution[0] + solution[1] - solution[2] + solution[3] - solution[4]           # Test values by plugging into original equations
eq2 = 2 * solution[0] + 2*solution[1] + solution[2] - solution[3] + solution[4]         
eq3 = 3 * solution[0] + solution[1] - 3*solution[2] - 2* solution[3] + 3 * solution[4]
eq4 = 4*solution[0] + solution[1] - solution[2] + 4*solution[3]- 5*solution[4]
eq5 = 16*solution[0] - solution[1] + solution[2] - solution[3]- solution[4]

print("Approximation of equation value using solutions found:" , eq1, eq2, eq3, eq4, eq5)        # Print values OF equations to see accuracy of approximation