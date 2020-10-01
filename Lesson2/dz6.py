products = []

# test data
products = [
    (1, {"название": "компьютер", "цена": 20000.0, "количество": 5, "eд": "шт."}),
    (2, {"название": "принтер", "цена": 6000.0, "количество": 2, "eд": "шт."}),
    (3, {"название": "сканер", "цена": 2000.0, "количество": 7, "eд": "шт."}),
    (4, {"название": "гвозди", "цена": 1042.0, "количество": 110, "eд": "кг."}),
    (5, {"название": "шурупы", "цена": 1650.0, "количество": 130, "eд": "кг."}),
    (6, {"название": "водка", "цена": 300.0, "количество": 200, "eд": "литры."}),
    (6, {"название": "спирт", "цена": 300.0, "количество": 200, "eд": "литры."})

]
###########

while True:
    name = input("Введите наименование товара: ")
    cost = float(input("Введите стоимость товара: "))
    count = int(input("Введите количество товара: "))
    unit = input("Введите единицу измерения: ")
    products.append(
        (len(products) + 1, {"название": name,
                             "цена": cost,
                             "количество": count,
                             "eд": unit})
    )
    if input("Вы хотите добавить еще? 'Нет'") == 'Нет':
        break

group_by = int(input("Сгрупировать по: Наименованию - 1, Цене - 2, ед.измерения - 3:   "))
if group_by == 1:
    group_by = "название"
elif group_by == 2:
    group_by = "цена"
else:
    group_by = "eд"

group = {}

for value in products:
    if group.__contains__(value[1][group_by]):
        group[value[1][group_by]].append(value)
    else:
        group[value[1][group_by]] = [value]

result = []

for value in group.values():
    name = []
    cost = []
    count = []
    unit = set()
    for prod in value:
        name.append(prod[1]["название"])
        cost.append(prod[1]["цена"])
        count.append(prod[1]["количество"])
        unit.add(prod[1]["eд"])
    result.append({"название": name, "цена": cost, "количество": count, "eд": unit})

for res in result:
    print(res)
