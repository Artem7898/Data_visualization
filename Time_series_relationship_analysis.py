import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Ваш код для получения данных о ценах акций
# Пример: случайные данные для иллюстрации
stock_prices = np.random.rand(5, 10)

sns.heatmap(stock_prices.T, cmap='YlGnBu', linewidths=.5)
plt.title('Тепловая карта цен акций')
plt.xlabel('Временные периоды')
plt.ylabel('Компании')
plt.show()
