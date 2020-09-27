name = "Bill"
print(type(name))

age = 30
print(type(age))

sex = False
print(type(sex))

salary = 34567.45
print(type(salary))

name = input("Input your name: ")
age = int(input("Input your age as number: "))
flag = True
while flag:
    sex = input("Input your sex as 'M' or 'F': ")
    if sex == 'M':
        sex = True
        flag = False
    elif sex == 'F':
        sex = False
        flag = False
    else:
        print("Your input is incorrect data. Please input 'M' or 'F'")
salary = float(input("Please input your salary: "))
print(f"Hello {name}\nYour sex is {'M' if sex else 'F'}\nYour age is {age}\nYour salary is {'%.2f' % salary}")
