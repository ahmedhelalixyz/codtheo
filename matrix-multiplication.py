
def mtrx_transpose(B):
    # Get dimensions
    row_dim_B = len(B)
    col_dim_B = len(B[0])

    # Create zero matrix using * operator
    BT = [[0] * row_dim_B for i in range(col_dim_B)]

    # Swap entries 
    for i in range(row_dim_B):
        for j in range(col_dim_B):
            BT[j][i] = B[i][j]
    
    return BT

def mtrx_multi(A, B):
    # Get dimensions
    row_dim_A = len(A)
    col_dim_A = len(A[0])
    row_dim_B = len(B)
    col_dim_B = len(B[0])

    # Check if dimensions are valid
    cols_A_vs_rows_B = col_dim_A == row_dim_B
    if not cols_A_vs_rows_B:
        print("Dimesnions are not Compatiable")
        return

    # Create empty matrix C
    ## Using list comprehension
    # C = [[0 for j in range(col_dim_B)] for i in range(row_dim_A)]
    
    ## Using * operator
    C = [[0] * col_dim_B for i in range(row_dim_A)]

    for i in range(col_dim_B):
        for j in range(row_dim_A):
            for k in range(col_dim_A):
                C[j][i] += A[j][k] * B[k][i]
            print(C)
            print("===========")   
    return C

A = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
B = [[1,2,3,4,5],[6,7,8,9,10]]
C = mtrx_multi(A, mtrx_transpose(B))

print("***************************************")
print(C)
