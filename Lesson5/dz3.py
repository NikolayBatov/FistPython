count_staff = 0
avr_salary = 0
last_name_staff = []

with open("dz3.txt", "r") as file:
    while True:
        staff = file.readline()
        if not staff:
            break
        staff = staff.split()
        if float(staff[1]) < 20000.00:
            last_name_staff.append(staff[0])
        avr_salary += float(staff[1])
        count_staff += 1

avr_salary = avr_salary / count_staff

print(f"Сотрудники с зарплатой ниже 20 000: {', '.join(last_name_staff)}.\nСредняя зарплата: {avr_salary:.2f}.")
