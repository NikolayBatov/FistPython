class ComplexNumber:

    def __init__(self, real: int, imaginary_unit: int) -> None:
        self.__real = real
        self.__imaginary_unit = imaginary_unit

    @property
    def real(self):
        return self.__real

    @property
    def imaginary_unit(self):
        return self.__imaginary_unit

    def __str__(self) -> str:
        return f"{self.__real} + {self.__imaginary_unit}j"

    def __add__(self, other):
        return ComplexNumber(self.__real + other.real, self.__imaginary_unit + other.imaginary_unit)

    def __mul__(self, other):
        return ComplexNumber(self.__real * other.real, self.__imaginary_unit * other.imaginary_unit)


comp_number = ComplexNumber(2, 3)
print(comp_number)
print(comp_number + ComplexNumber(3, 7))
print(comp_number * ComplexNumber(3, 7))