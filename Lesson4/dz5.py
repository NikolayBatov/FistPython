from random import randint
from functools import reduce

while True:
    try:
        count = int(input("Введите колличество сгенерируемых чисел: "))
        if count > 0:
            break
    except ValueError:
        print("Не валидный параметр!!!")

list_numbers = (randint(100, 1000) for _ in range(count))
print(reduce(lambda num1, num2: num1 * num2, list_numbers))
