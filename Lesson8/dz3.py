class ValueIsNotNumber(Exception):
    pass


def check_number(in_str):
    if not in_str.isdigit():
        raise ValueIsNotNumber(f'Error!!! Value: "{in_str}" is not number')
    return int(in_str)


list_number = []

while True:
    in_num = input("Введите число, для остановки введите 'stop': ")
    if in_num == 'stop':
        break
    try:
        in_num = check_number(in_num)
    except ValueIsNotNumber as ex:
        print(ex)
        continue
    list_number.append(in_num)

print(list_number)
