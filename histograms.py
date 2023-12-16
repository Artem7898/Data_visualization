import matplotlib.pyplot as plt

data = [85, 90, 92, 88, 78, 95, 89, 92, 94, 87, 78, 80, 92, 88, 94]

plt.hist(data, bins=10, edgecolor='black')
plt.title('Распределение оценок')
plt.xlabel('Оценки')
plt.ylabel('Частота')
plt.show()