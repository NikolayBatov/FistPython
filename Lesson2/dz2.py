variable = input("Please input data. For end, input 'end': ")
list_variable = []

while variable != "end":
    list_variable.append(variable)
    variable = input("Please input data again. For end, input 'end': ")

idx = 1
while len(list_variable) - 1 >= idx:
    tmp = list_variable[idx]
    list_variable[idx] = list_variable[idx - 1]
    list_variable[idx - 1] = tmp
    idx += 2
print(list_variable)
