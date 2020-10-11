def fact(num):
    if num > 1:
        f = 1
        for el in range(1, num + 1):
            f *= el
            yield f
    else:
        yield 1


print([el for el in fact(4)])
