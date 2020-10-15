class Worker:

    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = income

    def get_total_income(self) -> float:
        return self.__income["wage"] + self.__income["bonus"]


class Position(Worker):

    def __init__(self, name: str, surname: str, position: str, income: dict):
        super().__init__(name, surname, position, income)

    def get_full_name(self) -> str:
        return f"{self.name} {self.surname}"


position = Position("TestName", "TestSurname", "Staff", {"wage": 1234.34, "bonus": 4321.43})

print(position.get_full_name())
print(position.get_total_income())
