from sys import argv

separator = ''.join(['*' for _ in range(100)])

if len(argv) == 2 and argv[1] == '--help':
    print(f"{separator}\n"
          f"Пример: python3 dz1.py -h 44 -s 800 -p 42\n"
          f"-h - Выработка в часах. Принимаемое значение положительное чмсло\n"
          f"-s - Ставка за час. Принимаемое значение положительное чмсло\n"
          f"-p - Бонус в процентах. Принимаемое значение положительное чмсло или 0\n"
          f"!!!!ВСЕ ПАРАМЕТРЫ ОБЯЗАТЕЛЬНЫ!!!!\n"
          f"{separator}\n")
elif len(argv) != 7:
    print("Не переданы параметры!!! Предайте --help для помощи")
else:
    try:
        args = {param: float(argv[i]) for i, param in enumerate(argv[1:], 2) if i % 2 == 0}
        salary = args['-h'] * args['-s']
        salary = (salary + salary * (args['-p'] / 100)) if args['-p'] > 0 else salary
        print(f"Зарплата работника: {round(salary, 2)}\n"
              f"{separator}\n")
    except ValueError:
        print("Переданы не числовые значения!!! Предайте --help для помощи\n")
