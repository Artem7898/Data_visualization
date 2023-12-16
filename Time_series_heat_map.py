import seaborn as sns
import matplotlib.pyplot as plt

# Ваш код для получения данных о ценах акций
stock_prices = ...

sns.heatmap(stock_prices.T, cmap='YlGnBu', linewidths=.5)
plt.title('Тепловая карта цен акций')
plt.xlabel('Временные периоды')
plt.ylabel('Компании')
plt.show()