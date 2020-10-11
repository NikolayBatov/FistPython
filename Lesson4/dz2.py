from random import randint

while True:
    try:
        count = int(input("Введите колличество сгенерируемых чисел: "))
        if count > 0:
            break
    except ValueError:
        print("Не валидный параметр!!!")

list_numbers = [randint(0, 1000) for _ in range(count)]
print(f"Исходный список: {list_numbers}")
result = [list_numbers[i] for i, num in enumerate(list_numbers, 1) if i < len(list_numbers) and num < list_numbers[i]]
print(f"Результат: {result}")
