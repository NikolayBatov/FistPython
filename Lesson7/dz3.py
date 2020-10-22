class Cell:

    def __init__(self, count_cell) -> None:
        self.__cells = round(count_cell)

    @property
    def cells(self):
        return self.__cells

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        return Cell(self.cells - other.cells)

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(self.cells / other.cells)

    def make_order(self, count_cell):
        return ''.join(['*\n' if i % count_cell == 0 else '*' for i in range(1, self.cells + 1)])


cell = Cell(10)
print(cell.make_order(4))

cell1 = cell + Cell(2)
print(cell1.make_order(5))
