import seaborn as sns
import matplotlib.pyplot as plt

# Ваш код для получения данных и проведения кластерного анализа
data = ...

distance_matrix = ...  # Результат кластерного анализа

sns.heatmap(distance_matrix, cmap='viridis', linewidths=.5)
plt.title('Матрица расстояний в кластерном анализе')
plt.show()



