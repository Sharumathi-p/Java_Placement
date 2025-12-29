# Matrix Addition in Python

def matrix_addition(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    
    return result

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()

def main():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    
    matrix1 = []
    matrix2 = []
    
    print("\nEnter elements of first matrix:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Element [{i}][{j}]: "))
            row.append(element)
        matrix1.append(row)
    
    print("\nEnter elements of second matrix:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Element [{i}][{j}]: "))
            row.append(element)
        matrix2.append(row)
    
    result = matrix_addition(matrix1, matrix2)
    
    print("\nMatrix 1:")
    print_matrix(matrix1)
    
    print("\nMatrix 2:")
    print_matrix(matrix2)
    
    print("\nResult of Matrix Addition:")
    print_matrix(result)

if __name__ == "__main__":
    main()
