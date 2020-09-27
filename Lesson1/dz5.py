proceeds = float(input("Введите выручку: "))
firmCost = float(input("Введите издерки фирмы: "))

resultWork = proceeds - firmCost

print(f"Фирма отработала в {'прибль' if resultWork > 0 else 'убыток'}")

if resultWork > 0:
    print(f"Рентабельность составила {'%.4f' % (proceeds / firmCost)}")
    staffCount = int(input("Введите количество сотрудников: "))
    print(f"Прибыль на одного сотрудника составила: {'%.2f' % (resultWork / staffCount)}")