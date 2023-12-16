import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
temperature = [20, 22, 25, 24, 23, 22, 21, 20, 19, 18]

plt.plot(hours, temperature, marker='o')
plt.title('Изменение температуры в течение дня')
plt.xlabel('Часы')
plt.ylabel('Температура (°C)')
plt.grid(True)
plt.show()