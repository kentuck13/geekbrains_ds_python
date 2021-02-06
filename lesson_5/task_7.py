import numpy

firms = [{}, {}]
profits = []
with open('task_7.txt') as file:
    for line in file:
        line = line.replace('\n', '')
        firm_name, type_ownership, gain, cost = line.split(' ')

        profit = int(gain) - int(cost)

        if profit > 0:
            firms[0][firm_name] = profit
            profits.append(profit)

        print(firm_name, type_ownership, gain, cost, profit)

firms[1]['average_profit'] = numpy.median(profits)

print(firms)
