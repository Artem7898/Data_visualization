import matplotlib.pyplot as plt
import matplotlib.animation as animation
from itertools import count

plt.style.use('ggplot')

x_vals = []
y_vals = []

index = count()


def animate(i):
    x_vals.append(next(index))
    y_vals.append(your_data_point())  # Замените your_data_point() на вашу функцию для получения фактических показателей

    plt.cla()  # Очистка предыдущего графика
    plt.plot(x_vals, y_vals, label='Динамика', marker='o')
    plt.title('Анимированный линейный график')
    plt.xlabel('Шаги')
    plt.ylabel('Показатель')
    plt.legend()
    plt.tight_layout()


def your_data_point():
    # Здесь вы можете вставить код для получения фактических данных (например, из файла, API и т.д.)
    # Замените этот код на ваш реальный код
    return 10  # Пример: возвращаем значение 10, вы должны заменить это на ваш реальный код


if __name__ == "__main__":
    ani = animation.FuncAnimation(plt.gcf(), animate, interval=1000, cache_frame_data=False)
    plt.show()
