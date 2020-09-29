number = int(input("Please input positive number: "))
inputNumber = number
max = -1

while number > 10:
    tmp = number % 10
    if max < tmp:
        max = tmp
    number = number // 10
if max < number:
    max = number
print(f"Max digit in input number {inputNumber} is {max}")