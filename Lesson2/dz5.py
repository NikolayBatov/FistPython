rating_list = [8, 7, 5, 3, 3, 2]

while True:
    flag = True
    number = None
    while flag:
        number = input("Input number rating: ")
        if number.count("-") > 1 or not number.lstrip("-").isnumeric():
            print(f"Incorrect input!!! Input data '{number}' is not numeric")
            continue
        number = int(number)
        flag = False

    inx = 0
    while inx < len(rating_list):
        if rating_list[inx] <= number:
            rating_list.insert(inx, number)
            break
        elif inx == len(rating_list) - 1:
            rating_list.append(number)
            inx += 1
        inx += 1
    if input("If you won't out and print rating type 'end' or press Enter") == 'end':
        print(rating_list)
        break
