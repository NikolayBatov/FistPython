int_month = None
flag = True
list_seasons = ["Зима", "Весна", "Лето", "Осень"]
result = None
dict_seasons = {
    1: "Зима",
    2: "Зима",
    3: "Весна",
    4: "Весна",
    5: "Весна",
    6: "Лето",
    7: "Лето",
    8: "Лето",
    9: "Осень",
    10: "Осень",
    11: "Осень",
    12: "Зима"
}

while flag:
    int_month = input("Input month as numeric range 1-12: ")
    if int_month.count("-") > 1 or not int_month.lstrip("-").isnumeric():
        print(f"Incorrect input!!! Input data '{int_month}' is not numeric")
        continue
    int_month = int(int_month)
    if int_month < 1 or int_month > 12:
        print(f"Incorrect input!!! Input data value '{int_month}' is {'more 12' if int_month > 12 else 'less 1'}")
        continue
    flag = False

if 1 <= int_month <= 2 or int_month == 12:
    result = list_seasons[0]
elif 9 <= int_month <= 11:
    result = list_seasons[3]
elif 6 <= int_month <= 8:
    result = list_seasons[2]
else:
    result = list_seasons[1]

print(f"List in {result}")

result = dict_seasons[int_month]
print(f"Dict in {result}")
