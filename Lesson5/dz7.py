import json

dict_firms = {}
profit_sum = 0
profit_count = 0

with open("dz7.txt", "r") as r_file:
    while True:
        line = r_file.readline()
        if not line:
            break
        line = line.split()
        profit = int(line[2]) - int(line[3])
        dict_firms[line[0]] = profit
        if profit > 0:
            profit_sum += profit
            profit_count += 1

with open("dz7w.txt", "w") as w_file:
    json.dump([dict_firms, {"average_profit": round(profit_sum / profit_count, 2)}], w_file, sort_keys=True, indent=2)
