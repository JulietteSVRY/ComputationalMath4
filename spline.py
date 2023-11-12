from scipy.interpolate import CubicSpline
import colors as color
from graph_draw import *

print('\n' + color.BOLD + color.RED + "Решение функций методом интерполяции кубическими сплайнами.", color.END)
print(color.GREEN,
              "1: sin(x)", '\n',
              "2: cos(x ** 2 - 4 * x + 1)", '\n', color.END)

func = input(color.UNDERLINE + color.YELLOW + "Введите функцию: " + color.END)
a, b, k = map(float, input(color.UNDERLINE + color.YELLOW + "Введите интервал [a; b] и шаг [k]: " + color.END).split())


def f(x):
    return np.sin(x)

#def f(x):
#    return np.cos(x ** 2 - 4 * x + 1)


x = np.linspace(0, 2*np.pi, 10)
y = f(x) + 0.1*np.random.normal(size=len(x))


cs = CubicSpline(x, y)


x_fine = np.linspace(0, 2*np.pi, 100)
y_fine = f(x_fine)


x_interp = np.linspace(0, 2*np.pi, 100)
y_interp = cs(x_interp)


deviation = np.abs(f(x_interp) - y_interp)
max_deviation_idx = np.argmax(deviation)
max_deviation_point = (x_interp[max_deviation_idx], y_interp[max_deviation_idx])


error = np.linalg.norm(f(x_interp) - y_interp, ord=np.inf)


def calc(function: str, array: list[list]) -> None:
    plt.subplot(131)

    pop_max_deviation(function, array, subplot=131)


plt.plot(x_fine, y_fine, label='Исходная функция')
plt.plot(x, y, 'o', label='Заданные точки')
plt.plot(x_interp, y_interp, label='Интерполированная функция')
plt.plot(max_deviation_point[0], max_deviation_point[1], 'rx', label='Точка максимального отклонения')
plt.legend()
plt.show()

print(f"Погрешность метода: {error}")
print(f"Точка максимального отклонения: ({max_deviation_point[0]:.2f}, {max_deviation_point[1]:.2f})")

