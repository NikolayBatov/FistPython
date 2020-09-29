distance = float(input("Введите колличество км пройденых за первый день: "))
resultDistance = float(input("Введите желаемое колличество км: "))
countDay = 1

while distance < resultDistance:
    distance = distance + (distance * 0.1)
    countDay += 1
print(f"Ответ: на {countDay}-й день спортсмен достиг результата — не менее {'%.1f' % resultDistance} км.")
