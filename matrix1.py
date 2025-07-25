def input_matrix(rows, cols):
    matrix = []
    print("Enter elements row-wise:")
    for i in range(rows):
        row = []
        for j in range(cols):
            val = int(input(f"Enter element [{i+1}][{j+1}]: "))
            row.append(val)
        matrix.append(row)  # Fix: append row after it's fully populated
    return matrix

def display_matrix(matrix):
    for row in matrix:
        print(" ".join(str(x) for x in row))

def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

# Main program
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("\nMatrix 1:")
matrix1 = input_matrix(rows, cols)

print("\nMatrix 2:")
matrix2 = input_matrix(rows, cols)

print("\nMatrix 1:")
display_matrix(matrix1)

print("\nMatrix 2:")
display_matrix(matrix2)

sum_matrix = add_matrices(matrix1, matrix2)
print("\nSum of Matrix1 and Matrix2:")
display_matrix(sum_matrix)
