salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
money = 0
# Вычислим общие траты за 10 месяцев
for i in range(10):
    if i == 1:
        money = spend
    else:
        money = money + (spend * increase)
        spend = spend * increase
# Найдем необходимую сумму финансовой подушки
need_money = money - (salary * 10)
print(round(need_money))
