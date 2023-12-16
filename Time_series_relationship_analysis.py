import matplotlib.pyplot as plt

# Ваши данные о ценах акций
stock_prices_company_a = [100, 110, 95, 105, 120]
stock_prices_company_b = [90, 100, 85, 95, 110]

plt.scatter(stock_prices_company_a, stock_prices_company_b, color='green')
plt.title('Диаграмма рассеяния: Взаимосвязь цен акций двух компаний')
plt.xlabel('Цены акций Компания A')
plt.ylabel('Цены акций Компания B')
plt.show()