words = input("Input words: ").split()

for idx, word in enumerate(words):
    print(f"{idx + 1}. {word[:10]}")
