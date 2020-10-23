from abc import ABC


class IncorrectInput(Exception):
    pass


class Office:

    def __init__(self) -> None:
        self.__stock = {}
        self.__count_item = {}

    def __add_count(self, item):
        if not self.__count_item.__contains__(item.__class__.__name__):
            self.__count_item[item.__class__.__name__] = 1
        else:
            self.__count_item[item.__class__.__name__] += 1

    @property
    def statistic(self):
        return self.__count_item.copy()

    @property
    def stock(self):
        return self.__stock.copy()

    def add_item(self, departament, item):
        if not self.__stock.__contains__(departament):
            self.__stock[departament] = [item]
        else:
            self.__stock[departament].append(item)
        self.__add_count(item)

    def __str__(self) -> str:
        return '\n'.join([f"{key} -> {[str(item) for item in value]}" for key, value in self.__stock.items()])


class OfficeEquipment(ABC):
    __INV_NUMBER = 1

    def __init__(self, color: bool, formats: str) -> None:
        self._color = color
        self._formats = formats
        self._inv_number = OfficeEquipment.__INV_NUMBER
        OfficeEquipment.__INV_NUMBER += 1

    def __str__(self) -> str:
        return f"\tInv number: {self._inv_number} "


class Printer(OfficeEquipment):

    def __init__(self, color: bool, formats: str, _type: str) -> None:
        super().__init__(color, formats)
        self.__type = _type

    def __str__(self) -> str:
        return f"{super(Printer, self).__str__()} Printer - (is_color: {self._color}, format: {self._formats}, type: {self.__type})\n"


class Scanner(OfficeEquipment):

    def __str__(self) -> str:
        return f"{super(Scanner, self).__str__()} Scanner - (is_color: {self._color}, format: {self._formats})\n"


class Xerox(OfficeEquipment):

    def __init__(self, color: bool, formats: str, _type: str) -> None:
        super().__init__(color, formats)
        self.__type = _type

    def __str__(self) -> str:
        return f"{super(Xerox, self).__str__()} Printer - (is_color: {self._color}, format: {self._formats}, type: {self.__type})\n"


office = Office()
msg_menu = f"\033[31mСклад организации:\033[0m" \
           f"\n\t1 - Добавить на склад." \
           f"\n\t2 - Отчет колличесва." \
           f"\n\t3 - Отчет по департаментам." \
           f"\n\t4 - Выход." \
           f"\n\033[32mВведите номер операции: \033[0m"
msg_add_new_item = f"\033[31mДобавить на склад:\033[0m" \
                   f"\n\t1 - Принтер." \
                   f"\n\t2 - Сканер." \
                   f"\n\t3 - Ксерокс." \
                   f"\n\t4 - Назад." \
                   f"\n\033[32mВведите номер операции: \033[0m"


def validate_input(msg: str, count_value):
    while True:
        try:
            id_item = int(input(msg))
            if 1 > id_item > count_value:
                raise IncorrectInput()
            return id_item
        except ValueError:
            print("Ошибка. Введено не число.")
        except IncorrectInput:
            print(f"Ошибка. Введите число то 1 до {count_value}.")


def create_item(id_item):
    color = True if input("Цветной да/нет: ") == 'да' else False
    _format = input("Введите формат: ")
    if id_item == 1:
        _type = input("Введите тип печати: ")
        return Printer(color, _format, _type)
    elif id_item == 2:
        return Scanner(color, _format)
    elif id_item == 3:
        return Xerox(color, _format)


# office.add_item('test', Printer(True, 'A4', "Laser"))
# office.add_item('dep1', Printer(True, 'A4', "Laser"))
# office.add_item('test', Printer(True, 'A4', "Matr"))
# office.add_item('test', Scanner(True, 'A4'))
# office.add_item('dep2', Xerox(True, 'A4', "Laser"))

while True:
    value_chose = validate_input(msg_menu, 4)
    if value_chose == 1:
        value_id_item = validate_input(msg_add_new_item, 4)
        if value_id_item != 4:
            departament = input("Введите отдел: ")
            item = create_item(value_id_item)
            if item is not None:
                office.add_item(departament, item)
    elif value_chose == 2:
        print("\n".join([f'{key} - {value}шт.' for key, value in office.statistic.items()]))
    elif value_chose == 3:
        print("\n".join([f"Отдел: {key}:\n{''.join([str(item) for item in office.stock[key]])}" for key in office.stock.keys()]))
    elif value_chose == 4:
        break
