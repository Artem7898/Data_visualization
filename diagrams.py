import matplotlib.pyplot as plt

labels = ['Львы', 'Тигры', 'Слоны', 'Обезьяны', 'Пингвины']
sizes = [15, 10, 25, 20, 30]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Это делает круг круглым, а не овальным
plt.title('Распределение видов животных в зоопарке')
plt.show()