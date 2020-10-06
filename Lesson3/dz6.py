def int_func_v1(word):
    return word.title()


def int_func_v2(word):
    return chr(ord(word[0]) - 32) + word[1:]


words = input("Введите слова: ").split()

result = [int_func_v1(word) for word in words]
print(" ".join(result))

result = [int_func_v2(word) for word in words]
print(" ".join(result))
