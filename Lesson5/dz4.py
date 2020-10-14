my_dict = {'1': 'Один', '2': 'Два', '3': 'Три', '4': 'Четыре'}

with open("dz4w.txt", "w") as w_file:
    with open("dz4.txt", "r") as r_file:
        while True:
            line = r_file.readline()
            if not line:
                break
            line = line.split()
            line[2] = my_dict.get(line[2])
            w_file.write(f'{" ".join(line)}\n')
