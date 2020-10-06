def check_number(msg, is_negative=False):
    number = input(msg)
    while True:
        if is_negative and 0 < number.count("-") <= 1 and number.lstrip("-").isdigit():
            return int(number)
        elif not is_negative and number.isdigit():
            return int(number)
        else:
            print("Введено не коректное значение!!!!")
            number = input(msg)


def my_pow(fist, second):
    result = fist
    for value in range(1, abs(second)):
        result *= fist
    return 1 / result


fist_number = check_number("Введите число возводимое в степень: ")
second_number = check_number("Введите отрицательную степень : ", True)
print(my_pow(fist_number, second_number))
