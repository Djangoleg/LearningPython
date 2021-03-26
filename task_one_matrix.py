class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        matrix_string = str()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                matrix_string += f"{self.matrix[i][j]} "
            matrix_string += '\n'
        return matrix_string

    def __add__(self, other):
        return Matrix([
            [cell_1 + cell_2 for cell_1, cell_2 in zip(row_1, row_2)]
            for row_1, row_2 in zip(self.matrix, other.matrix)
        ])


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])
print(matrix_1 + matrix_2)