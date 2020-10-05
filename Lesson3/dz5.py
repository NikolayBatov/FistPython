def check_numbers(list_numbers):
    if "and" in list_numbers or "AND" in list_numbers:
        return map(float, list_numbers[:list_numbers.index("and" or "AND")]), True
    else:
        return map(float, list_numbers), False


result = []
while True:
    try:
        numbers = check_numbers(
            input("Введите числа в одну строку, разделитель пробел, для завершения введите and: ").split())
        if numbers[1]:
            result += list(numbers[0])
            break
        else:
            result += list(numbers[0])
    except ValueError:
        print("Значения могут быть только числа или 'and' - для завершения")

print(sum(result))
