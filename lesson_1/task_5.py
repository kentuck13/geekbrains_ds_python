billing = int(input('Input your billing: '))
costs = int(input('Input your costs: '))
profit = billing - costs

if profit > 0:
    print('You are in plus.')
else:
    print('You are in minus.')

employees_count = int(input('Input employees count: '))
salary = profit / employees_count

print('Salary of each employee is %d' % salary)
