  # Input 3x3 matrix
matrix = []
print("Enter elements of 3x3 matrix row-wise:")
for i in range(3):
    row = list(map(int, input(f"Enter row {i+1} elements separated by space: ").split()))
    matrix.append(row)

# Compute transpose
transpose = []
for i in range(3):
    trans_row = []
    for j in range(3): 
        trans_row.append(matrix[j][i])
    transpose.append(trans_row)

# Display original matrix
print("Original Matrix:")
for row in matrix:
    print(row)

# Display transpose 
print("Transpose of Matrix:")
for row in transpose:
    print(row)
