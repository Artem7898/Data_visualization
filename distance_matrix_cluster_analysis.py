import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Ваши данные
data = {'Company A': [0, 1, 2, 3, 4],
        'Company B': [1, 0, 3, 2, 5],
        'Company C': [2, 3, 0, 1, 4],
        'Company D': [3, 2, 1, 0, 5]}

distance_matrix = pd.DataFrame(data)

sns.heatmap(distance_matrix, cmap='viridis', linewidths=.5)
plt.title('Матрица расстояний в кластерном анализе')
plt.show()










