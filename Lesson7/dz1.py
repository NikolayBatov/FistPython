class Matrix:

    def __init__(self, matrix: list) -> None:
        self.matrix = matrix

    def __str__(self) -> str:
        return '\n'.join([' '.join(map(str, i)) for i in self.matrix])

    def __add__(self, other):
        result = []
        for i in zip(self.matrix, other.matrix):
            row = []
            for j in zip(i[0], i[1]):
                row.append(sum(j))
            result.append(row)
        return Matrix(result)


matrix1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix2 = Matrix([[7, 8], [9, 10], [11, 12]])
# print(matrix1)
# print()
# print(matrix2)
# print()
print(matrix1 + matrix2)

