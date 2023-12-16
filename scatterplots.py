import matplotlib.pyplot as plt

# Ваши данные
sales = [100, 120, 90, 110, 130]
advertising_costs = [50, 60, 45, 55, 70]

plt.scatter(advertising_costs, sales, color='blue')
plt.title('Диаграмма рассеяния: Затраты на рекламу vs. Объем продаж')
plt.xlabel('Затраты на рекламу')
plt.ylabel('Объем продаж')
plt.show()