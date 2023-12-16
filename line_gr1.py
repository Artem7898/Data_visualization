import matplotlib.pyplot as plt

months = ['Янв', 'Фев', 'Мар', 'Апр', 'Май']
product_a_sales = [100, 120, 90, 110, 130]
product_b_sales = [80, 100, 110, 120, 95]
product_c_sales = [120, 130, 110, 100, 90]

plt.plot(months, product_a_sales, label='Продукт A', marker='o')
plt.plot(months, product_b_sales, label='Продукт B', marker='o')
plt.plot(months, product_c_sales, label='Продукт C', marker='o')

plt.title('Сравнение продаж продуктов')
plt.xlabel('Месяцы')
plt.ylabel('Продажи')
plt.legend()
plt.grid(True)
plt.show()