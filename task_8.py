money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

while money_capital > ((spend * increase) - salary):  # пока финансовая подушка больше, чем превышение трат
    all_money = salary + money_capital
    if all_money > (spend * increase):
        month += 1
        if month >= 1:
            money_capital = money_capital - ((spend * increase) - salary)
            spend = spend * increase
        else:
            money_capital = money_capital - (spend - salary)

print(month)
