from random import randint

sum_all_number = 0

with open("dz5w.txt", "w") as w_file:
    for i in range(10):
        list_int = []
        for j in range(10):
            list_int.append(randint(1, 10000))
        w_file.write(f'{" ".join(map(str, list_int))}\n')

with open("dz5w.txt", "r+") as rw_file:
    sum_number = []
    while True:
        line = rw_file.readline()
        if not line:
            break
        sum_number += map(int, line.split())
        sum_all_number = sum(sum_number)
    rw_file.write(f"\nСумма чисел равна: {sum_all_number}")

print(f"Сумма чисел равна: {sum_all_number}")