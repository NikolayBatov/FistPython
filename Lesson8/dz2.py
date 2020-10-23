class DivisionByZero(Exception):
    pass


def get_num(msg, is_divider=False):
    while True:
        try:
            num = float(input(msg))
            if is_divider and num == 0:
                raise DivisionByZero()
            return num
        except ValueError as val:
            print('Введено не число')
        except DivisionByZero:
            print('Ошибка!!! Деление на 0')


fist_number = get_num("Введите делимое: ")
second_number = get_num("Введите делитель: ", True)

print(fist_number / second_number)