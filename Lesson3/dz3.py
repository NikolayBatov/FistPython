def my_func(number1, number2, number3):
    result = {number1, number2, number3}
    result.remove(min(result))
    return sum(result)


def get_number(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Введено не число!!!")


print(my_func(get_number("Введите первое число: "),
              get_number("Введите второе число: "),
              get_number("Введите третье число: ")))
