def my_division(fist, second):
    return fist / second


result = None
while True:
    try:
        result = my_division(float(input("Введите делимое: ")), float(input("Введите делитель: ")))
        break
    except ZeroDivisionError:
        print("Ошибка!! Деление на 0")
    except ValueError:
        print("Введено не число!!!!")

print(result)
