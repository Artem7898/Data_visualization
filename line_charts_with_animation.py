import matplotlib.pyplot as plt
import matplotlib.animation as animation
from itertools import count

plt.style.use('seaborn-darkgrid')

x_vals = []
y_vals = []

index = count()


def animate(i):
    x_vals.append(next(index))
    y_vals.append(your_data_point)  # Замените your_data_point на ваш фактический показатель

    plt.plot(x_vals, y_vals, label='Динамика', marker='o')
    plt.title('Анимированный линейный график')
    plt.xlabel('Шаги')
    plt.ylabel('Показатель')
    plt.legend()


ani = animation.FuncAnimation(plt.gcf(), animate, interval=1000)  # 1000 миллисекунд = 1 секунда
plt.show()