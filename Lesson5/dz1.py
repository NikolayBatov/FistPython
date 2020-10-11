with open("dz1.txt", "w") as file:
    while True:
        words = input("Введите строку: ")
        if not words:
            break
        file.write(f"{words}\n")
