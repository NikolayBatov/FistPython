count_lines = 0
count_words = 0

with open("dz2.txt", "r") as file:
    while True:
        line = file.readline()
        if not line:
            break
        count_lines += 1
        count_words += len(line.split())

print(f"Файл содержит {count_lines} строк и {count_words} слов.")
