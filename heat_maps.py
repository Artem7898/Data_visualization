import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Пример данных
data = {'Variable1': [1, 2, 3, 4, 5],
        'Variable2': [5, 4, 3, 2, 1],
        'Variable3': [2, 3, 1, 5, 4],
        'Variable4': [4, 1, 5, 2, 3]}

# Создаем DataFrame
df = pd.DataFrame(data)

# Вычисляем корреляционную матрицу
correlation_matrix = df.corr()

# Строим тепловую карту
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Корреляционная тепловая карта')
plt.show()




