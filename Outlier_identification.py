import matplotlib.pyplot as plt

# Ваши данные
profits = [100, 120, 90, 110, 130, 500]

plt.scatter(range(len(profits)), profits, color='red')
plt.title('Диаграмма рассеяния: Прибыль компаний')
plt.xlabel('Компании')
plt.ylabel('Прибыль')
plt.show()