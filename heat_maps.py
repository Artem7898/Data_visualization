import seaborn as sns
import matplotlib.pyplot as plt

# Ваш код для получения данных
data = ...

correlation_matrix = data.corr()

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Корреляционная тепловая карта')
plt.show()