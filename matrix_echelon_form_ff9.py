# Define the finite field F_8 = F_2[a]/(a^3 + a + 1)
K.<a> = GF(3**2, name='a', modulus=x^2 + 2*x + 2)

# Display all elements of the field
print("Elements of F_9:")
for i, elem in enumerate(K):
    print("{}: {}".format(i, elem))
print()

# Display addition table with polynomial representations
print("Addition table for F_9 (in terms of a where a^2 + a + 1 = 0):")
print(K.addition_table(names='elements'))
print()

# Display multiplication table with polynomial representations
print("Multiplication table for F_8 (in terms of a where a^3 + a + 1 = 0):")
print(K.multiplication_table(names='elements'))
print()

def matrix_to_echelon(matrix, show_steps=True):
    """
    Reduce a matrix to row echelon form over F_8
    
    Args:
        matrix: A matrix over the finite field K
        show_steps: Boolean to show intermediate steps
    
    Returns:
        The row echelon form of the matrix
    """
    # Make a copy to avoid modifying the original
    A = copy(matrix)
    m, n = A.dimensions()
    
    if show_steps:
        print("Original matrix:")
        print(A)
        print()
    
    current_row = 0
    
    for col in range(n):
        # Find pivot in current column
        pivot_row = None
        for row in range(current_row, m):
            if A[row, col] != 0:
                pivot_row = row
                break
        
        # If no pivot found, move to next column
        if pivot_row is None:
            continue
            
        # Swap rows if needed
        if pivot_row != current_row:
            A.swap_rows(current_row, pivot_row)
            if show_steps:
                print(f"Swapped rows {current_row} and {pivot_row}:")
                print(A)
                print()
        
        # Make pivot = 1 (multiply row by inverse of pivot)
        pivot = A[current_row, col]
        if pivot != 1:
            A[current_row] = A[current_row] * (pivot^(-1))
            if show_steps:
                print(f"Scaled row {current_row} by {pivot^(-1)} to make pivot = 1:")
                print(A)
                print()
        
        # Eliminate entries below pivot
        for row in range(current_row + 1, m):
            if A[row, col] != 0:
                multiplier = A[row, col]
                A[row] = A[row] - multiplier * A[current_row]
                if show_steps:
                    print(f"Row {row} = Row {row} - ({multiplier}) * Row {current_row}:")
                    print(A)
                    print()
        
        current_row += 1
        if current_row >= m:
            break
    
    return A

def matrix_to_reduced_echelon(matrix, show_steps=True):
    """
    Reduce a matrix to reduced row echelon form (RREF) over F_8
    
    Args:
        matrix: A matrix over the finite field K
        show_steps: Boolean to show intermediate steps
    
    Returns:
        The reduced row echelon form of the matrix
    """
    # First get to echelon form
    A = matrix_to_echelon(matrix, show_steps)
    m, n = A.dimensions()
    
    if show_steps:
        print("Now reducing to reduced row echelon form...")
        print()
    
    # Work backwards to eliminate entries above pivots
    for row in range(m-1, -1, -1):
        # Find the pivot column for this row
        pivot_col = None
        for col in range(n):
            if A[row, col] != 0:
                pivot_col = col
                break
        
        if pivot_col is None:
            continue
            
        # Eliminate entries above the pivot
        for above_row in range(row):
            if A[above_row, pivot_col] != 0:
                multiplier = A[above_row, pivot_col]
                A[above_row] = A[above_row] - multiplier * A[row]
                if show_steps:
                    print(f"Row {above_row} = Row {above_row} - ({multiplier}) * Row {row}:")
                    print(A)
                    print()
    
    return A

# Example usage with a sample matrix
print("="*50)
print("EXAMPLE: Matrix reduction over F_8")
print("="*50)

# Create a sample matrix over F_8
sample_matrix = matrix(K, [
    [a^6, a^2, a^4, 1, a^4],
    [a^7, 1, a^4, a^5, a^6],
    [1, a^2, a^4, a^6, a],
    [a^4, a^7, a^4, a^7, a^2]
])

print("Sample matrix over F_8:")
print(sample_matrix)
print()

# Reduce to echelon form
print("STEP 1: Reducing to row echelon form")
print("-" * 40)
echelon_form = matrix_to_echelon(sample_matrix, show_steps=False)

print("Final row echelon form:")
print(echelon_form)
print()

# Reduce to reduced echelon form
print("STEP 2: Reducing to reduced row echelon form")
print("-" * 40)
rref_form = matrix_to_reduced_echelon(sample_matrix, show_steps=True)

print("Final reduced row echelon form:")
print(rref_form)
print()

# Verification using SageMath's built-in function
print("VERIFICATION:")
print("-" * 20)
sage_rref = sample_matrix.rref()
print("SageMath's rref():")
print(sage_rref)
print("Our result matches SageMath:", rref_form == sage_rref)
