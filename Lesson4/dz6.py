from itertools import count
from itertools import cycle


def get_values(gen, count_result):
    return [next(gen) for _ in range(count_result)]

while True:
    try:
        amount = int(input("Введите колличество сгенерируемых чисел: "))
        if amount > 0:
            break
    except ValueError:
        print("Не валидный параметр!!!")

int_iter = count(amount)
obj_iter = cycle([chr(let) for let in range(65, 91)])

print(get_values(obj_iter, amount))
print(get_values(int_iter, amount))
