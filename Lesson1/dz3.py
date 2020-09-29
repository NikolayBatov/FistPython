inputNumber = input("Please input number: ")
tmp = inputNumber
calculation = inputNumber
result = 0
index = 0
while index < 3:
    if index > 0:
        tmp += inputNumber
        calculation += f" + {tmp}"
    result += int(tmp)
    index += 1

print(f"Calculation {calculation} = {result}")