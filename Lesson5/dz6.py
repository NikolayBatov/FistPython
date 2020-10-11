my_dict = dict()


def sum_h(l_hours):
    if len(l_hours) >= 1:
        try:
            value = l_hours.pop()
            return int(value[:value.find('(')]) + sum_h(l_hours)
        except ValueError:
            return sum_h(l_hours)
    else:
        return 0


with open("dz6.txt", "r") as r_file:
    while True:
        line = r_file.readline()
        if not line:
            break
        line = line.split()
        my_dict[line[0][:-1]] = sum_h(line[1:])

print(my_dict)
